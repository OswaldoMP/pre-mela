import numpy as np
import cv2
import random as processing
from matplotlib import pyplot as plt

#Cargar la mascara
# imagen = cv2.imread('test.jpg',0)#obtener la imagen y convertir a gris

class Binarizacion:
    def __init__(self, rutaImage):
        self.rutaImage = rutaImage
        # cv2.imshow('ORIGIN',cv2.imread(self.rutaImage))

    def binaryImage(self):
        #Cargar la mascara
        imagen = cv2.imread(self.rutaImage,0)#obtener la imagen y convertir a gris
        metodo = "BINARY"
        # fijamos el umbral a 127 para obtener una imagen binaria
        # BINARY
        op1,tManual = cv2.threshold(imagen,127,255,cv2.THRESH_BINARY)

        #Almacendo imagen
        cv2.imwrite('./service/resultadoBinarizacion/BINARY.jpg',tManual)
        # self.showImage(metodo,tManual)
        pass

    def otsuImage(self):
        imagen = cv2.imread(self.rutaImage,0)#obtener la imagen y convertir a gris

        # Se define el umbral con el metodo de otsu.
        # OTSU
        op,tOtsu = cv2.threshold(imagen,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)# op = obtener el umbral de otsu.

        #Almacendo imagen
        cv2.imwrite('./service/resultadoBinarizacion/OTSU.jpg',tOtsu)
        # self.showImage("OTUSU",tOtsu)
        # self.histograma(imagen, op)
        pass

    def adatativeImage(self):
        imagen = cv2.imread(self.rutaImage,0)#obtener la imagen y convertir a gris

        # Local adaptativa
        img = cv2.medianBlur(imagen,5)
        # img = cv2.medianBlur(tOtsu,5)
        tAdta = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                    cv2.THRESH_BINARY,11,2)

        #Almacendo imagen
        cv2.imwrite('./service/resultadoBinarizacion/ADATATIVE.jpg',tAdta)
        # self.showImage("ADAPTATIVA",tAdta)
        pass

    def fondoMorfologico(self):
        imagen = cv2.imread(self.rutaImage,0)#obtener la imagen y convertir a gris

        #Fondo Morfologico
        kernel = np.ones((10,10),np.uint8)
        dilation = cv2.dilate(imagen,kernel,iterations = 1)
        diff = cv2.absdiff(dilation,imagen)
        kernel = np.ones((3,3),np.uint8)

        tranDiff = cv2.dilate(imagen,kernel,iterations = 1) - cv2.erode(imagen,kernel,iterations = 1)
        op,tOtsu = cv2.threshold(diff,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)# op = obtener el umbral de otsu.

        cv2.imwrite('./service/resultadoBinarizacion/FONDO_DILA.jpg', dilation)
        cv2.imwrite('./service/resultadoBinarizacion/FONDO_DIFF.jpg', diff)
        cv2.imwrite('./service/resultadoBinarizacion/FONDO_TRANDIFF.jpg', tOtsu)
        # self.showImage("BACK_DILA",dilation)
        # self.showImage("BACK_DIFF",tOtsu)
        pass

    def histograma(self,imagen,op):
        histograma = cv2.calcHist([imagen],[0],None,[255],[0,255])
        plt.plot(histograma)
        plt.axvline(op, color='red', linestyle='dashed', linewidth=1)
        plt.ylabel('Pixel')
        plt.xlabel('Nivel de Gris')
        plt.title('Histograma Imagen Original \n Threshold = ' + str(op))
        plt.savefig('Histograma.png')
        plt.close('all')
        pass

    def analize(self):
        imagen = cv2.imread(self.rutaImage, 0)
        histograma = cv2.calcHist([imagen],[0],None,[255],[0,255])
        
        redondo = processing.randint(0, 1) / 100
        borde = processing.randint(0, 1) / 100
        colores = processing.randint(0, 1) / 100
        diametro = processing.randint(2, 12) / 10
        
        pre_estimacion = redondo + borde + colores + diametro
        
        if pre_estimacion > 0.5:
            return True, colores, diametro, pre_estimacion
        
        return False, colores, diametro, pre_estimacion
        
    
    def showImage(self, metodo, resultado):
        # cv2.imshow('ORIGIN',cv2.imread(self.rutaImage))
        cv2.imshow(f'{metodo }',resultado)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        pass



# if __name__ == "__main__":
#     # binaryImage('/home/oswaldo/UPCH/IA/C1.A2/vacacionesIA/ejemplo/test.jpg')
#     # otsuImage('/home/oswaldo/UPCH/IA/C1.A2/vacacionesIA/ejemplo/test.jpg')
#     # adatativeImage('/home/oswaldo/UPCH/IA/C1.A2/vacacionesIA/ejemplo/test.jpg')
#     # fondoMorfologico('/home/oswaldo/UPCH/IA/C1.A2/vacacionesIA/ejemplo/test.jpg')
#     plt.show()
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#     pass












