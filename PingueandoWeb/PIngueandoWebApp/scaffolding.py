from generic_scaffold import CrudManager
from PIngueandoWebApp import models

class PinguerCrudManager(CrudManager):
    model = models.Pinguer
    prefix = 'pinguers'

class PinguerEventCrudManager(CrudManager):
    model = models.PinguerEvent
    prefix = 'pinguersevents'