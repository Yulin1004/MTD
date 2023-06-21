#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2014-2022 Megvii Inc. All rights reserved.
import torch
import torch.nn as nn

from exps.model.tal_head import TALHead
from exps.model.dfp_pafpn import DFPPAFPN


class YOLOX(nn.Module):
    """
    YOLOX model module. The module list is defined by create_yolov3_modules function.
    The network returns loss values from three YOLO layers during training
    and detection results during test.
    """

    def __init__(self, backbone=None, head_0=None,head_1=None,head_2=None):
        super().__init__()
        if backbone is None:
            backbone = DFPPAFPN()
        if head_0 is None:
            head_0 = TALHead(20)
        if head_1 is None:
            head_1 = TALHead(20)
        if head_2 is None:
            head_2 = TALHead(20)

        self.backbone = backbone
        self.head_0 = head_0
        self.head_1 = head_1
        self.head_2 = head_2


    def forward(self, x, targets=None, buffer=None, mode='off_pipe',delay = 0):
        # fpn output content features of [dark3, dark4, dark5]
        assert mode in ['off_pipe', 'on_pipe']

        if mode == 'off_pipe':
            with torch.no_grad():
                fpn_outs = self.backbone(x, buffer=buffer, mode='off_pipe')
            if self.training:
                assert targets is not None
                if(delay == 0):
                    loss, iou_loss, conf_loss, cls_loss, l1_loss, num_fg = self.head_0(
                        fpn_outs, targets, x
                    )
                elif(delay == 1):
                    loss, iou_loss, conf_loss, cls_loss, l1_loss, num_fg = self.head_1(
                        fpn_outs, targets, x
                    )
                else:
                    loss, iou_loss, conf_loss, cls_loss, l1_loss, num_fg = self.head_2(
                        fpn_outs, targets, x
                    )
                outputs = {
                    "total_loss": loss,
                    "iou_loss": iou_loss,
                    "l1_loss": l1_loss,
                    "conf_loss": conf_loss,
                    "cls_loss": cls_loss,
                    "num_fg": num_fg,
                }
            else:
                if(delay == 0):
                    outputs = self.head_0(fpn_outs)
                elif (delay == 1):
                    outputs = self.head_1(fpn_outs)
                else:
                    outputs = self.head_2(fpn_outs)

            return outputs
        elif mode == 'on_pipe':
            fpn_outs, buffer_ = self.backbone(x,  buffer=buffer, mode='on_pipe')
            if(delay == 0):
                outputs = self.head_0(fpn_outs)
            elif (delay == 1):
                outputs = self.head_1(fpn_outs)
            else:
                outputs = self.head_2(fpn_outs)
            
            return outputs, buffer_




