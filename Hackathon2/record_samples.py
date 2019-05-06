#Will take arguments as user_name
#hardcoding sampling rate to 8000

#--user <user_name>
import Record_audio as rec
import sys
import keyboard as kb

sounds_to_record = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five',
'Six', 'Seven', 'Eight', 'Nine', 'Yes', 'No']

if len(sys.argv) < 2:
	print('Required syntax: python record_samples.py <user_name>')
	exit
	
user = sys.argv[1]

print("\n-----Start the process to record samples for User:", user)

for label in range(0,12):
    label = 10
    print("\n\n--------------Starting to record samples for ", sounds_to_record[label])
    for sample_id in range(0,5):
        print('{}_{}_{}.wav'.format( label, user, sample_id))
        print("\nPress 'n' when you are ready")
        kb.wait('n')
        rec.record_voice(user, label, sample_id, "group5_voice/" )