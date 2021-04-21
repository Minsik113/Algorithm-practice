'''
고양이인지 구분하는 모델 만들기

오리지날 VGG16 모델 만들어보자
'''

def VGG_16():
    model = Sequential()
    model.add(Lambda(vgg_preprocess, input_shape=(3,224,224)))

    ConvBlock(2, model, 64)
    ConvBlock(2, model, 128)
    ConvBlock(3, model, 256)
    ConvBlock(3, model, 512)
    ConvBlock(3, model, 512)
    
    model.add(Flatten())
    FCBlock(model)
    FCBlock(model)
    model.add(Dense(1000, activation='softmax'))
    return model

def ConvBlock(layers, model, filters):
    for i in range(layers):
        model.add(ZeroPadding2D((1,1)))
        model.add(Convoltion2D(filters, 3, 3, activation='reulu'))
    model.add(MaxPooling2D((2, 2), strides=(2, 2)))            

def FCBlock(model):
    model.add(Dense(4096, activation='relu'))
    model.add(Dropout(0.5))

model = VGG_16()
model.compile(optimizer=Adam(lr=0.001),
                loss='categorical_crossentropy', metrics=['accuracy'])

'''
ConvBlock: 
    1. 사이즈 안줄어들게 가장자리 채워주려고 zero패딩
    2. 3x3사이즈 패턴으로, filter 갯수만큼 패턴을 찾겠다.
    3. activation은 ReLU
    4. 위의 Conv를 layers수만큼 겹겹히 쌓는다.
    5. for문이 끝나고 사이즈 줄여주려고 Maxpooling한다.
FCBlock
    1. 출력 4096짜리 Fully COnnected NN이다.
    2. ReLU쓰고
    3. 오버피팅방지로 Dropout을 함
VGG_16
    -ConvBlock
    1. Conv + Maxpooling덩어리를 filter개수 늘리면서 그림사이즈는 점점 줄어들게 쌓아올렸다.
    2. 이걸 FC에 넣으려고 Flatten함
    - FCBlock
    3. 마지막에 1000개 출력인데 이중 하나 고르는(category문제)니까 softmax를 사용.
    4. 길찾는 방법은 믿고쓰는 Adam
'''
