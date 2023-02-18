from django.db import models
from django.contrib.auth.models import User
from .utils import sendTransaction
import hashlib

""" QUANDO FAI MODIFICHE AI MODELLI APPLICA MIGRATION A DB!!! """

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, unique=True)
    text = models.TextField()
    hash = models.CharField(max_length=64, default='leave blank (any changes will be ignored) ', null=False) # editable=false non va bene perchè toglie il campo anche in modifica (non lo voglio modificare ma almeno così posso vederlo, poi ignoro le modifiche)
    txId = models.CharField(max_length=66, default='leave blank (any changes will be ignored)', null=False)
    # readonly_fields = ['hash', 'txId'] # not working

    def writeOnChain(self):
        self.hash = hashlib.sha256((self.text + self.code).encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
    
    def save(self, *args, **kwargs):
        print('self._state.adding: ', self._state.adding)
        # self._state.adding == True when creating, False when updating
        # in case of updating do nothing
        if self._state.adding: 
            self.writeOnChain()
            super(Product, self).save(*args, **kwargs)