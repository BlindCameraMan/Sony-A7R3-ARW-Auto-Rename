# Sony A7R3 ARW Auto-Rename

Using Phil Harvey's [Exiftool](https://exiftool.org/) and [PyExiftool](https://github.com/sylikc/pyexiftool) by sylikc this script scans the current directory for Sony .ARW files and extracts the shot date and time, shot type, exposure compensation, shot number and sequence number and renames the files in the following formats:

 - **Single Shot**: DateTime_OriginalName
		2026-07-22_16-54-03_DSC04443.ARW
 - **Exposure Bracketing**: DateTime_Bracket_SeqNumberOfSeqTotal_ExpComp_OriginalName
2026-07-17_15-04-33_DSC04286.ARW
2026-07-17_15-11-54_Bracket_1of9_-2.7EV_DSC04374.ARW
2026-07-17_15-11-54_Bracket_2of9_-2EV_DSC04375.ARW
2026-07-17_15-11-55_Bracket_3of9_-1.3EV_DSC04376.ARW
2026-07-17_15-11-55_Bracket_4of9_-0.7EV_DSC04377.ARW
2026-07-17_15-11-55_Bracket_5of9_0EV_DSC04378.ARW
2026-07-17_15-11-55_Bracket_6of9_0.7EV_DSC04379.ARW
2026-07-17_15-11-55_Bracket_7of9_1.3EV_DSC04380.ARW
2026-07-17_15-11-56_Bracket_8of9_2EV_DSC04381.ARW
 - **WB_Bracket**: DateTime_WB_Bracket_SeqNumberOfSeqTotal_OriginalName
 2026-07-19_13-16-55_WB_Bracket_1of3_DSC04389.ARW
2026-07-19_13-16-55_WB_Bracket_2of3_DSC04390.ARW
2026-07-19_13-16-55_WB_Bracket_3of3_DSC04391.ARW
2026-07-19_13-17-43_WB_Bracket_1of3_DSC04392.ARW
2026-07-19_13-17-43_WB_Bracket_2of3_DSC04393.ARW
2026-07-19_13-17-43_WB_Bracket_3of3_DSC04394.ARW
 - **DRO**: DateTime_DRO_Bracket_SeqNumberOfSeqTotal_OriginalName
 2026-07-17_15-13-19_DRO_Bracket_1of3_DSC04383.ARW
2026-07-17_15-13-19_DRO_Bracket_2of3_DSC04384.ARW
2026-07-17_15-13-19_DRO_Bracket_3of3_DSC04385.ARW
2026-07-18_09-06-01_DRO_Bracket_1of3_DSC04386.ARW
2026-07-18_09-06-01_DRO_Bracket_2of3_DSC04387.ARW
2026-07-18_09-06-01_DRO_Bracket_3of3_DSC04388.ARW
 - **Burst**: DateTime_BURST_SeqNumberOfSeqTotal_OriginalName
2026-07-22_16-51-57_Burst_1of4_DSC04398.ARW
2026-07-22_16-51-57_Burst_2of4_DSC04399.ARW
2026-07-22_16-51-57_Burst_3of4_DSC04400.ARW
2026-07-22_16-51-57_Burst_4of4_DSC04401.ARW
The script will list all the renames and ask to confirm before the rename is initiated.

You will need exiftool installed from as well as PyExiftool before this script will run. Please see the links above on how to install both.