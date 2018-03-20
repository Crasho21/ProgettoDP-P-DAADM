# Progetto Data Protection & Privacy And Data Analisys And Data Mining

## Dataset
### Il dataset utilizzato è quello di BAdDroIds. (https://sites.google.com/view/baddroids)

## Core
### Il progetto consiste nell'effettuare mining sul dataset per identificare quali apk sono malware e quali no.
### Il dataset è stato anonimizzato attraverso l'utilizzo della K-Anonimity per confrontare i risultati ottenuti in base al tipo di anonimizzazione applicata.

## Anonimizzazione
### Sono stati individuati 326110 quasi identifiers ed applicati due diversi approcci di anonimizzazione, uno per i permessi ed uno per le API.
###
### Permessi:
#### P2 = permission
####
#### P1 = normal
####
#### P0 = android.permission.WAKE_LOCK
####
### API:
#### A3 = api
####
#### A2 = android.app
####
#### A1 = android.app.Service
####
#### A0 = android.app.Service->\<init>

## Mining:
### L’algoritmo utilizzato per effettuare la fase di mining si basa sui minimi quadrati regolarizzati one vs one 
