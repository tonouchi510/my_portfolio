from keras.utils import to_categorical
from keras.models import model_from_json
import numpy as np
from PIL import Image


class digit_recognizer:

    def __init__(self):
        # モデルのロード
        self.model = model_from_json(open('myapps/mnist/static/mnist/model/mnist_model.json').read())
        self.model.load_weights('myapps/mnist/static/mnist/model/mnist_model.h5')
        self.model.compile(loss='categorical_crossentropy', optimizer='adam')

    def summary(self):
        return self.model.summary()

    def predict(self, X_path):
        X = np.array(Image.open('./myapps/mnist/static'+X_path))
        X = self.normalize(X)
        X = np.reshape(X, (1, 28, 28, 1))
        pred = self.model.predict(X)
        return np.argmax(pred)

    def relearning(self, X_path, y):
        X = np.array(Image.open('./myapps/mnist/static'+X_path))
        X = self.normalize(X)
        X = np.reshape(X, (1, 28, 28, 1))
        y = to_categorical(y, num_classes=10)
        self.model.fit(X, y)
        # モデルの保存
        model_json_str = self.model.to_json()
        open('myapps/mnist/static/mnist/model/mnist_model.json', 'w').write(model_json_str)
        self.model.save_weights('myapps/mnist/static/mnist/model/mnist_model.h5')

    def normalize(self, X):
        return X / X.max()

