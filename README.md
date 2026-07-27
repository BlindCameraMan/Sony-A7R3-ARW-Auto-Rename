# Sony A7R3 ARW Auto-Rename

Using Phil Harvey's [Exiftool](https://exiftool.org/) and [PyExiftool](https://github.com/sylikc/pyexiftool) by sylikc this script scans the current directory for Sony .ARW files and extracts the shot date and time, shot type, exposure compensation, shot number and sequence number and renames the files in the following formats:

 - **Single Shot**: DateTime_OriginalName
 - **Exposure Bracketing**: DateTime_Bracket_SeqNumberOfSeqTotal_ExpComp_OriginalName
 - **WB_Bracket**: DateTime_WB_Bracket_SeqNumberOfSeqTotal_OriginalName
 - **DRO**: DateTime_DRO_Bracket_SeqNumberOfSeqTotal_OriginalName
 - **Burst**: DateTime_BURST_SeqNumberOfSeqTotal_OriginalName

The script will list all the renames and ask to confirm before the rename is initiated.

You will need exiftool installed from as well as PyExiftool before this script will run. Please see the links above on how to install both.