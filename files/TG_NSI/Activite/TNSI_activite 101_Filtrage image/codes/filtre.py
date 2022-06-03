import PIL.Image as Image

class Filtre :
    
    def __init__(self, img):
        self.__img = img
        self.__pix = self.__img.load()
        
    def size(self) : 
        return self.__img.size
    
    def width(self):
        return self.size()[0]
    
    def height(self) :
        return self.size()[1]
    
    def weight(self) :
        return self.width * self.height
    
    def get_pix(self, col, row) :
        return self.__pix[col,row]
    
    def __set_pix(self, col, row, value) :
        self.__pix[col, row] = value
    
    def __save_pixels(self) :
        for l in range(self.height()) :
            for c in range(self.width()) :
                self.__img .putpixel((c,l),self.get_pix(c,l))
    
    def reverse(self) :
        reverse = [0]*3
        for l in range(self.height()) :
            for c in range(self.width()) :
                for i in range(3) :
                    reverse[i] = 255 - self.get_pix(c, l)[i]
                self.__set_pix(c,l,tuple(reverse))
        self.__save_pixels()
    
    def red(self) :
        red = [0]*3
        for l in range(self.height()) :
            for c in range(self.width()) :
                red[0] = self.get_pix(c, l)[0]
                self.__set_pix(c,l,tuple(red))
        self.__save_pixels()

    def color2grey(self) :
        sum = 0
        for l in range(self.height()) :
            for c in range(self.width()) :
                pix = self.get_pix(c, l)
                for i in range(3) :
                    sum += pix[i]
                self.__set_pix(c,l,(int(sum/3),int(sum/3),int(sum/3)))
                sum = 0
        self.__save_pixels()
        
    def threshold(self,val) :
        self.color2grey()
        for l in range(self.height()) :
            for c in range(self.width()) :
               
                if self.get_pix(c, l)[0] < val : self.__set_pix(c,l,(0,0,0))
                else : self.__set_pix(c,l,(255,255,255))              
        self.__save_pixels()

img = Image.open('tigre.jpg')

pixels = img.load()