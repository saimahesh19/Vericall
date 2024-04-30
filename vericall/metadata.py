# from pydub.utils import mediainfo
# import datetime

# def retrieve_call_info(audio_file):
#     # Extracting metadata using pydub
#     metadata = mediainfo(audio_file)
    
#     # Printing available metadata tags
#     print("Available Metadata Tags:")
#     for tag, value in metadata.items():
#         print(f"{tag}: {value}")
    
#     # Timestamps
#     start_time_str = metadata.get('TAG:creation_time')
#     if start_time_str:
#         start_time = datetime.datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
#         end_time = start_time + datetime.timedelta(seconds=float(metadata['duration']))
#         duration = end_time - start_time
#     else:
#         start_time = None
#         end_time = None
#         duration = None
    
#     # Device Information
#     device_model = metadata.get('TAG:device_model')
#     device_id = metadata.get('TAG:device_id')
#     os_version = metadata.get('TAG:os_version')
#     recording_software = metadata.get('TAG:recording_software')
    
#     # Call Information
#     caller_number = metadata.get('TAG:caller_number')
#     callee_number = metadata.get('TAG:callee_number')
#     call_duration = metadata.get('duration')
#     call_start_time = start_time
#     call_end_time = end_time
#     call_type = metadata.get('TAG:call_type')
#     call_quality_metrics = metadata.get('TAG:call_quality_metrics')
    
#     # Location Data
#     gps_coordinates = metadata.get('TAG:gps_coordinates')
#     location_name = metadata.get('TAG:location_name')
    
#     # File Information
#     file_format = metadata.get('file_format')
#     file_size = metadata.get('file_size')
#     bitrate = metadata.get('bit_rate')
#     sample_rate = metadata.get('sample_rate')
    
#     return {
#         "Timestamps": {
#             "Start time": start_time,
#             "End time": end_time,
#             "Duration": duration
#         },
#         "Device Information": {
#             "Device model": device_model,
#             "Device ID": device_id,
#             "Operating system/version": os_version,
#             "Software/app used for recording": recording_software
#         },
#         "Call Information": {
#             "Caller's phone number or identifier": caller_number,
#             "Callee's phone number or identifier": callee_number,
#             "Call duration": call_duration,
#             "Call start time": call_start_time,
#             "Call end time": call_end_time,
#             "Call type": call_type,
#             "Call quality metrics": call_quality_metrics
#         },
#         "Location Data": {
#             "GPS coordinates": gps_coordinates,
#             "Location name or address": location_name
#         },
#         "File Information": {
#             "File format": file_format,
#             "File size": file_size,
#             "Bitrate": bitrate,
#             "Sample rate": sample_rate,
#             "Duration": call_duration
#         }
#     }

# # Provide the path to your audio file
# audio_file = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\vericall\10-86.mp3"
# call_info = retrieve_call_info(audio_file)
# print(call_info)

from pydub.utils import mediainfo

def print_audio_metadata(audio_file):
    # Extracting metadata using pydub
    metadata = mediainfo(audio_file)
    
    # Printing available metadata tags and their values
    print("Available Metadata Tags:")
    for tag, value in metadata.items():
        print(f"{tag}: {value}")

# Example usage:
audio_file = r"C:\Users\SAI MAHESH\Desktop\files\semisters\sem6\prj\forensics\vericall\10-86.mp3"
print_audio_metadata(audio_file)
