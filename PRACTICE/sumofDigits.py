'''
###############
1.
def summ(num,add):
    if num==0:
        return add
    rem=num%10
    add+=rem
    return summ(num//10,add)
print(summ(123,0))

##########
2.
number1=int(input('enter 1st number'))
number2=int(input('enter 2nd number'))
number1=number1 * number2
number2=number1 // number2
number1=number1 // number2
print(number1,number2)

##############
3.
s='fhdflshbfslkhfbslkfbhslfjhbsdvsJKBEFWEGWUYRTWGRUWOFWGEUIFBWDFWDBFHWJDVFHJKasdwtuknfiitngjt75378595hf75hr74h'
d={}
for ch in s:
   d[ch]=s.count(ch)
print(d)
'''
################
'''Images Pixels are in form of pixels so i am taking array'''
# Arr=[[1,2,3],[4,5,6],[7,8,9]]
# Transpose_Arr=[]
# for i in range(0,len(Arr)):
#     new_arr=[]
#     for j in range(0,len(Arr)):
#         new_arr.append(Arr[j][i])
#     Transpose_Arr.append(new_arr)
# print(Transpose_Arr)
#####################
'''
#print BMW as output
variable=["Bus", "car",{"Bus":["car", "bus",{"car":"bus", "Car":["bus", "car", ["BMW"]],},"Bus"]},"Bus"]
print(variable[2]['Bus'][2]['Car'][-1])
'''

import json
with open('results.json','r') as fo:
    jo=json.load(fo)
    #print(jo)
encoded=json.dumps(jo, indent=4)
decoded=json.loads(encoded)
frames_per_video={}
missing_frames_per_video={}
for video_id, video_data in jo.items():
    frames=len(video_data)
    frames_per_video[video_id]=frames
    #print(frames_per_video)
    missing_frames=[i for i in range(1,frames+1) if str(i) not in video_data]
    if missing_frames:
        missing_frames_per_video[video_id]=missing_frames
max_vehical_video={}
max_person_video={}
for video_id, video_data in jo.item():
    pass






















variable=["Bus", "car", {"Bus":["car", "bus", {"car":"bus", "Car":["bus", "car", ["BMW"]],
},"Bus"]},"Bus"]