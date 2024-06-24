
import tkinter
from datetime import datetime

window = tkinter.Tk()
window.title('타자 연습')
window.geometry('400x600+100+100')

counter = 0
text = [
'별 헤는 밤',
'계절이 지나가는 하늘에는',
'가을로 가득 차 있습니다.',
'나는 아무 걱정도 없이',
'가을 속의 별들을 다 헤일 듯합니다.',
'가슴속에 하나둘 새겨지는 별을',
'이제 다 못 헤는 것은',
'쉬이 아침이 오는 까닭이요,',
'내일 밤이 남은 까닭이요,',
'아직 나의 청춘이 다하지 않은 까닭입니다.',
'별 하나에 추억과',
'별 하나에 사랑과',
'별 하나에 쓸쓸함과',
'별 하나에 동경과',
'별 하나에 시와',
'별 하나에 어머니, 어머니,',
'어머님, 나는 별 하나에 아름다운 말 한마디씩 불러 봅니다.',
'소학교 때 책상을 같이 했던 아이들의 이름과,',
'패, 경, 옥, 이런 이국 소녀들의 이름과,',
'벌써 아기 어머니 된 계집애들의 이름과,',
'가난한 이웃 사람들의 이름과,',
'비둘기, 강아지, 토끼, 노새, 노루, 프랑시스 잠,',
'라이너 마리아 릴케 이런 시인의 이름을 불러 봅니다.',
'이네들은 너무나 멀리 있습니다.',
'별이 아스라이 멀듯이.',
'어머님,',
'그리고 당신은 멀리 북간도에 계십니다.',
'나는 무엇인지 그리워',
'이 많은 별빛이 내린 언덕 위에',
'내 이름자를 써 보고',
'흙으로 덮어 버리었습니다.',
'딴은 밤을 새워 우는 벌레는',
'부끄러운 이름을 슬퍼하는 까닭입니다.',
'그러나 겨울이 지나고 나의 별에도 봄이 오면',
'무덤 위에 파란 잔디가 피어나듯이',
'내 이름자 묻힌 언덕 위에도',
'자랑처럼 풀이 무성할 거외다.'
]

start_time = None
total_characters = 0
current_text = None
wroung_word = 0
right_word = 0

def start():
    global counter
    global start_time
    global total_characters
    counter = 0
    start_time = datetime.now()
    total_characters = 0

    start_timer()
    initialize_text()

def start_timer():
    global counter
    if counter < 5 * 60 and text: # 5 minutes
        counter += 1
        minutes = counter // 60
        seconds = counter % 60
        timer.config(text=f'시간 : {minutes:02}:{seconds:02}')
        window.after(1000, start_timer)
    else:
    # 타이머가 종료되면 메시지 박스로 알림
        if not text:
            messagebox.showinfo('타이머 종료', '시간이 초과되었습니다.\n더 이상 입력할 수 없습니다.')

def initialize_text():
    update_text()
text_ = ''
def update_text():
    global text_
    if text:
        current_text = text.pop(0)
        count = len(current_text)
        text_ = current_text
        new_label.config(text=f'현재 텍스트 길이: {count}\n{current_text}')
    else:
        new_label.config(text='더 이상 텍스트가 없습니다.')

def update_label(event=None):
    global total_characters
    global text_
    global wroung_word
    global right_word

    new_text = entry1.get()

    #text_ 원래글자
    #new_text 입력글자

    text_ = str(text_)
    for i, x in enumerate(text_):
        if len(new_text) < len(text_):
            new_text = new_text + "_" * (-len(new_text)+len(text_))
        if new_text[i] != x:
            wroung_word += 1
        else:
            right_word += 1
    rate = right_word / (right_word + wroung_word) * 100

    label_2.config(text = f'정확도 : {rate:.2f}%')

    current_lines = label_3.cget("text").strip().split('\n')
    max_lines = 20 # 최대 표시할 라인 수
    if len(current_lines) >= max_lines:
        current_lines.pop(0)
    
    current_lines.append(new_text)
    label_3.config(text='\n'.join(current_lines))
    
    entry1.delete(0, tkinter.END)
    update_text()
    
    # 입력된 글자 수 업데이트
    total_characters += len(new_text)
    
    # 현재 타수 업데이트
    update_typing_speed()

def update_typing_speed():
    global start_time
    if start_time:
        elapsed_time = (datetime.now() - start_time).total_seconds() / 60 # 분 단위로 변환
        typing_speed = total_characters / elapsed_time if elapsed_time > 0 else 0 # 분당 타자수 계산
        label_1.config(text=f'현재 타수: {typing_speed*2:.1f} 타') # 소수점 첫째 자리까지 표시

label_1 = tkinter.Label(window, text='현재 타수 : ', width=25)
label_2 = tkinter.Label(window, text='정확도 : ', width=25)
new_label = tkinter.Label(window, text='여기에 추가할 내용을 입력하세요')
label_3 = tkinter.Label(window, text='', justify='left')

label_4 = tkinter.Button(window, text='시작하기', command=start)
timer = tkinter.Label(window, text='시간 : 00:00')

label_1.grid(row=0, column=0, columnspan=2)
label_2.grid(row=0, column=2, columnspan=2)
new_label.grid(row=2, column=0, columnspan=4)
label_3.grid(row=3, column=0, columnspan=4)
timer.grid(row=1, column=0, columnspan=2)
label_4.grid(row=1, column=2, columnspan=2)

entry1 = tkinter.Entry(window)
entry1.grid(row=5, column=0, columnspan=4)

entry1.bind("<Return>", update_label)

window.mainloop()