#Exiftool information to keep track of
"""
https://exiftool.sourceforge.net/TagNames/Sony.html
SequenceImageNumber: Total images in the burst/bracket set.
SequenceFileNumber: The current image's position (e.g., 1 of 17).
ReleaseMode2: The core drive mode identifier (Continuous, Bracket, etc.).
ExposureCompensation: Used for calculating EV offset in brackets.
DynamicRangeOptimizerBracket: Identifies DRO bracketing.
command line for testing:
exiftool -n -G -EXIF:DateTimeOriginal -SequenceImageNumber -SequenceFileNumber -SequenceLength -ReleaseMode -ReleaseMode2 -ReleaseMode3 -ExposureCompensation -DynaicRangeOptimizer -DynamicRangeOptimizerBracket *.arw"""
import os
import exiftool
from exiftool import ExifToolHelper
burst_sequences = {}
current_burst_key = None
prev_seq_num = None
burst_counter = 0
pixel_shift_enabled = False
pixel_shift_group = None
prev_pixel_shift_group = None
pixel_shift_seq_num = None
pixel_shift_seq_len = None
pixel_shift_seq_ID = None
prev_pixel_shift_seq_ID = None
pixel_shift_group_num = 0
photo_tags = [
    "EXIF:DateTimeOriginal",
    "MakerNotes:SequenceImageNumber",
    "MakerNotes:SequenceLength",
    "MakerNotes:ReleaseMode",
    "MakerNotes:ReleaseMode2",
    "EXIF:ExposureCompensation",
    "MakerNotes:DynamicRangeOptimizer",
    "MakerNotes:DynamicRangeOptimizerBracket",
    "MakerNotes:PixelShiftInfo",
    ]
# print("Moving To Test Direcotry")
# os.chdir('test photos\Pixelshift')
print("ARW Rename Script")
print("Last Updated: Oct 15 2026")
print("Searching for ARW files in: ", os.getcwd())
        
#Find ARW files and put them in a list called arw_files
arw_files = []
with os.scandir() as ArwListEntries:
 for entry in ArwListEntries:
  if entry.is_file() and entry.name.lower().endswith('.arw'):
   arw_files.append(entry.name)
#print(arw_files)
print("Number of ARW Files is", len(arw_files))
#Scan for the tags needed in metadata with pyexiftool.
#scan list arw_files for photo_tags
rename_queue = []
file_data_list = [] 
with ExifToolHelper() as et:
     all_data = list(et.get_tags(arw_files, tags=photo_tags))
#      print(all_data)
     for i, data in enumerate(all_data):
        filename = data.get('SourceFile')
        date_raw = data.get('EXIF:DateTimeOriginal')
        rel_mode_raw = data.get('MakerNotes:ReleaseMode')
        rel_mode_2_raw = data.get('MakerNotes:ReleaseMode2')
        seq_num = data.get('MakerNotes:SequenceImageNumber')
        seq_len = data.get('MakerNotes:SequenceLength')
        exp_comp = data.get('EXIF:ExposureCompensation')
        pixel_shift_raw = data.get('MakerNotes:PixelShiftInfo')

                # Format Date/Time
                # Converts "2026:07:18 09:06:01" to "2026-07-18_09-06-01" because you can't have : in filenames
        if date_raw:
            try:
                date_part, time_part = date_raw.split(' ')
                iso_date_part = date_part.replace(':', '-') # Using dashes for file safety
                iso_time_part = time_part.replace(':', '-') # Using dashes for file safety
                iso_datetime = f"{iso_date_part}_{iso_time_part}"
            except ValueError:
                iso_datetime = date_raw.replace(':', '-')
        else:
            iso_datetime = "NoDate"
        if pixel_shift_raw == "00000000 0 0 0x0":
            pixel_shift_enabled = False
#             pixel_shift_group = None
#             prev_pixel_shift_group = None
#             pixel_shift_seq_num = None
#             pixel_shift_seq_len = None
#             pixel_shift_seq_ID = None
#             prev_pixel_shift_seq_ID = None
        if pixel_shift_raw != "00000000 0 0 0x0":
            try:
#                 print(pixel_shift_raw)
                pixel_shift_group, pixel_shift_seq_num, pixel_shift_seq_len, pixel_shift_seq_ID = pixel_shift_raw.split(' ', 3)
                pixel_shift_enabled = True
                if ((pixel_shift_group != prev_pixel_shift_group) and (pixel_shift_seq_ID != prev_pixel_shift_seq_ID)) or pixel_shift_group_num == 0:
                    pixel_shift_group_num = pixel_shift_group_num + 1
                    prev_pixel_shift_group = pixel_shift_group
                    prev_pixel_shift_seq_ID = pixel_shift_seq_ID
                else:
                    pixel_shift_group_num = pixel_shift_group_num
#                 print(pixel_shift_enabled, pixel_shift_group, pixel_shift_seq_num, pixel_shift_seq_len, pixel_shift_seq_ID)
            except ValueError:
                pixel_shift_enabled = False
# for data in all_data:
        file_entry = {
            'filename': filename,
            'iso_datetime': iso_datetime,
            'rel_mode_raw': rel_mode_raw,
            'rel_mode_2_raw': rel_mode_2_raw,
            'seq_num': seq_num,
            'seq_len': seq_len,
            'exp_comp': exp_comp,
            'pixel_shift_enabled': pixel_shift_enabled,
            'pixel_shift_group': pixel_shift_group,
            'pixel_shift_seq_num': pixel_shift_seq_num,
            'pixel_shift_seq_len': pixel_shift_seq_len,
            'pixel_shift_seq_ID': pixel_shift_seq_ID,
            'pixel_shift_group_num': f'{pixel_shift_group_num:03}'
        }
        file_data_list.append(file_entry)
#             print(f"Added {file_entry['filename']} (List Length: {len(file_data_list)})")
        # Determine shot type
# print(file_data_list)
file_data_list.sort(key=lambda x: x['filename'])
for i, item in enumerate(file_data_list):
#         print(f"{i+1}: {item['filename']}")
# for item in file_data_list:
        # Unpack variables
        filename = item['filename']
        iso_datetime = item['iso_datetime']
        rel_mode_raw = item['rel_mode_raw']
        rel_mode_2_raw = item['rel_mode_2_raw']
        seq_num = item['seq_num']
        seq_len = item['seq_len']
        exp_comp = item['exp_comp']
        pixel_shift_enabled = item['pixel_shift_enabled']
        pixel_shift_group = item['pixel_shift_group']
        pixel_shift_seq_num = item['pixel_shift_seq_num']
        pixel_shift_seq_len = item['pixel_shift_seq_len']
        pixel_shift_seq_ID = item['pixel_shift_seq_ID']
        pixel_shift_group_num = item['pixel_shift_group_num']
        # Prepare filename components
        name_base, ext = os.path.splitext(filename)
        new_filename = ""
        new_name_base = ""
        name_base, ext = os.path.splitext(filename)
        Shot_Type =(
                "BURST" if (rel_mode_raw == 2) and (rel_mode_2_raw == 1) else
                "EXPOSURE_BRACKETING" if (rel_mode_raw == 5) and (rel_mode_2_raw == 2) else
                "WB_Bracket" if (rel_mode_raw == 6) and (rel_mode_2_raw == 3) else
                "DRO" if (rel_mode_raw == 8) and (rel_mode_2_raw == 3) else
                "Pixel_Shift" if (pixel_shift_enabled == True) else
                "Single")
            # Format: DateTime_Burst_SeqOfTotal_OriginalName
        if Shot_Type == "BURST":
            new_burst_detected = False 

            if seq_num is not None:
                # Condition 1: Sequence number reset (e.g., 5 -> 1)
                if prev_seq_num is not None and seq_num <= prev_seq_num:
                    new_burst_detected = True
#                     print(f"  [RESET DETECTED] {filename}: Seq {prev_seq_num} -> {seq_num}")
                
                # If new burst, create a new unique key
                if new_burst_detected:
                    burst_counter += 1
                    current_burst_key = f"Burst_{burst_counter}_{iso_datetime}"
                elif current_burst_key is None:
                    # First file initialization
                    burst_counter += 1
                    current_burst_key = f"Burst_{burst_counter}_{iso_datetime}"
                
                # Create list for this burst if needed
                if current_burst_key not in burst_sequences:
                    burst_sequences[current_burst_key] = []
                
                burst_sequences[current_burst_key].append({
                    'filename': filename,
                    'seq_num': seq_num,
                    'release_mode': rel_mode_raw,
                    'name_base': name_base,
                    'iso_datetime': iso_datetime
                })
                
                # Update previous for next iteration
                prev_seq_num = seq_num
            
            else:
                # Not a burst shot or missing tag
                current_burst_key = None
                prev_seq_num = None
        elif Shot_Type == "EXPOSURE_BRACKETING":
        # Format: DateTime_Bracket_SeqOfTotal_ExpComp_OriginalName
            exp_str = str(exp_comp) if exp_comp is not None else "0"
            new_name_base = f"{iso_datetime}_Bracket_{seq_num}of{seq_len}_{exp_str}EV_{name_base}"
        elif Shot_Type == "WB_Bracket":
                # Format: DateTime_WB_Bracket_SeqOfTotal_OriginalName
                new_name_base = f"{iso_datetime}_WB_Bracket_{seq_num}of{seq_len}_{name_base}"
        elif Shot_Type == "DRO":
                # Format: DateTime_DRO_Bracket_SeqOfTotal_OriginalName
                new_name_base = f"{iso_datetime}_DRO_Bracket_{seq_num}of{seq_len}_{name_base}"
        elif Shot_Type == "Pixel_Shift":
                new_name_base = f"{iso_datetime}_Pixel_Shift_{pixel_shift_group_num}_{pixel_shift_seq_num}of{pixel_shift_seq_len}_{name_base}"
        else:
                # Single Shot: DateTime_OriginalName
                new_name_base = f"{iso_datetime}_{name_base}"

        if Shot_Type != "BURST" and (filename != new_filename):
            new_filename = f"{new_name_base}{ext}"
            rename_queue.append((filename, new_filename))
            # Queue for renaming
#                 print(f"Rename: {filename} -> {new_filename}")
#         if (Shot_Type != "BURST")
#             rename_queue.append((filename, new_filename)) if (Shot_Type != "BURST")
#         else:
#                     print(f"Skip (No change): {filename}")
        i + 1
for key, shots in burst_sequences.items():
                shots.sort(key=lambda x: x['seq_num'])
                count = len(shots)
#                 print(f"\n{key} (Total: {count})")
                for shot in shots:
                    filename = shot['filename']
                    iso_datetime = shot['iso_datetime']
                    name_base = shot['name_base']
                    seq_num = shot['seq_num']
#                     print(f"  {shot['seq_num']} of {count}: {shot['filename']}")
                    if (seq_num and count) != 1:
                        new_name_base = f"{iso_datetime}_Burst_{shot['seq_num']}of{count}_{name_base}"
                        new_filename = f"{new_name_base}{ext}"
                    if (seq_num == 1) and (count == 1):
                        new_name_base = f"{iso_datetime}_{name_base}"
                        new_filename = f"{new_name_base}{ext}"
                    if filename != new_filename:
#                         print(f"Rename: {filename} -> {new_filename}")
                        rename_queue.append((filename, new_filename))
                    else:
                        print(f"Skip (No change): {filename}")
                    
#Rename Files
if rename_queue:
    print("\n" + "="*60)
    print(f"Ready to rename {len(rename_queue)} files!")
    print("="*60)
    i = 0
    for old, new in rename_queue:
        old_display = old
        new_display = new
        i = i + 1
        print(f"'Image:', {i}, {old_display}  ->  {new_display}")
    confirm = input("Rename? '(y/n)")
    if confirm.strip().lower() == "y":
        print("\n--- Executing Renames ---")
        for old, new in rename_queue:
            try:
                os.rename(old, new)
                print(f"Success: {old} -> {new}")
            except FileExistsError:
                print(f"Error: Destination already exists: {new}")
            except Exception as e:
                print(f"Error renaming {old}: {e}")
            print("\nRenaming complete.")
    else:
        print("\nRename cancelled!")
else:
    print("\nNo files renamed.")