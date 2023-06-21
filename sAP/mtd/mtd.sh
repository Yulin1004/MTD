dataDir="../../data"  # path/to/your/data
config="../../cfgs/l_s50_onex_mtd_dfp_tal_filp.py" # path/to/your/cfg
weights="../../ckpts/mtd_l_s50_one_x.pth"  # path/to/your/checkpoint_path

save="modify_no_delay"
scale=0.5

python mtd_det.py \
	--data-root "$dataDir/Argoverse-1.1/tracking" \
	--annot-path "$dataDir/Argoverse-HD/annotations/val.json" \
	--fps 30 \
	--weights $weights \
	--in_scale 0.5 \
	--no-mask \
	--out-dir "$dataDir/mtd/online_resuklt/$save" \
	--overwrite \
	--config $config \
    --delay 0 \
   &&
python mtd_eval.py \
	--data-root "$dataDir/Argoverse-1.1/tracking" \
	--annot-path "$dataDir/Argoverse-HD/annotations/val.json" \
	--fps 30 \
	--eta 0 \
	--result-dir "$dataDir/mtd/online_resuklt/$save" \
	--out-dir "$dataDir/mtd/online_resuklt/$save" \

