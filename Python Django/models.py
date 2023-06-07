from django.db import models

class Book(models.Model):
      Name=models.CharField(max_length=20)
      Mobile=models.CharField(max_length=20)
      Address=models.CharField(max_length=80)
      Checkin=models.CharField(max_length=20,help_text=u'Stay start')
      Checkout=models.CharField(max_length=20,help_text=u'Leaving date')     

      def s(self):
          return '{}'.format(self.Name,self.Mobile,self.Address,self.Checkin,self.Checkout)

      @property
      def name_label(self):
          return self.__get_label('Name')
