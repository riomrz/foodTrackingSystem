from django.db import models
from django.contrib.auth.models import User
from .utils import sendTransaction
import hashlib

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=50)
    text = models.TextField()
    hash = models.CharField(max_length=64, default=None, null=True) # editable=false non va bene perchè toglie il campo anche in modifica
    txId = models.CharField(max_length=66, default=None, null=True)
    # readonly_fields=('hash', 'txId') # non funzia

    def writeOnChain(self):
        self.hash = hashlib.sha256(self.text.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
    
    def save(self, *args, **kwargs):
        print('self._state.adding: ', self._state.adding)
        # self._state.adding == True when creating, False when updating
        # in case od updating we do nothing
        if self._state.adding: 
            self.writeOnChain()
            super(Product, self).save(*args, **kwargs)
        