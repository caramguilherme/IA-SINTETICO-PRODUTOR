# -*- coding: utf-8 -*-
CORES=[
 "during the first sentence of the take she raises her left forearm from her lap, pivoting at the elbow, so that her left hand rises on the right side of the frame to shoulder height, palm facing the camera, holding up three fingers (index, middle and ring finger extended, thumb and little finger folded), holds them steady for about two seconds, makes one slow nod during the second sentence and lowers the hand onto her right knee during the final sentence",
 "she keeps a serious, firm, steady gaze during the whole take, makes one slow small shake of the head during the first sentence, and keeps her left hand resting on her right knee",
 "she gives one slow nod during the first sentence of the take, then during the second sentence she raises her left hand from her lap to shoulder height on the right side of the frame and opens it palm toward the camera, holds it for about two seconds and lowers it onto her right knee",
 "during the first sentence of the take she raises one finger of her left hand to shoulder height on the right side of the frame, during the second sentence she points that finger straight at the lens, and during the final sentence she lowers the hand onto her right knee while keeping her gaze firm",
 "she makes one firm shake of the head during the first sentence of the take, then during the second sentence she raises her left hand from her lap to shoulder height on the right side of the frame and points her left index finger at the lens, holds the point for one second and lowers the hand onto her right knee",
 "during the first sentence of the take she gives one slow nod, then during the second sentence she raises her left hand from her lap to shoulder height on the right side of the frame with the palm open and facing upward, holds it steady for about two seconds and lowers it onto her right knee",
 "during the first sentence of the take she raises one finger of her left hand to shoulder height on the right side of the frame, during the second sentence she keeps it steady, during the third sentence she raises a second finger beside it, and in the last second she lowers the hand onto her right knee",
 "during the first sentence of the take she raises her left hand from her lap and points her left index finger straight at the lens at shoulder height on the right side of the frame, holds a firm steady gaze, and lowers the hand onto her right knee during the final sentence",
 "she raises her left hand from her lap to shoulder height on the right side of the frame and opens it palm toward the camera with a half smile, holds it open for about three seconds and then gently lowers it onto her right knee",
]

def lines(L30):
    out=[L30(c) for c in CORES]
    # T3: o texto da fala diz "right hand" e "until the end": usar outras palavras no prefixo e no sufixo
    out[2]=out[2].replace("her right hand keeps holding","the hand on the left side of the frame keeps holding").replace("from the end of the last sentence of the take until the clip ends","from the final word of the take to the last frame of the clip")
    return out
