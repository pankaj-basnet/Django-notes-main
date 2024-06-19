=============================================================================
=============================================================================
=============================================================================
=============================================================================


saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (main)
$ cd crudProject

saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ ls -a
./  ../  crudApp/  crudProject/  manage.py*

saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ cd crudApp

saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject/crudApp (main)
$ ls -a
./  ../  __init__.py  admin.py  apps.py  migrations/  models.py  tests.py  views.py

saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject/crudApp (main)
$ cd ../cc/
bash: cd: ../cc/: No such file or directory

saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject/crudApp (main)
$ cd ../../

saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (main)
$ ls -a
./  ../  .git/  crudProject/  requirements.txt  r---requirements-txt-----on-june19---done-.txt  venv-240619-1445-/

saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (main)
$ git add .

saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (main)
$ git commit -am "created django project and app"
[main d956810] created django project and app
 15 files changed, 217 insertions(+)
 create mode 100644 crudProject/crudApp/__init__.py
 create mode 100644 crudProject/crudApp/admin.py
 create mode 100644 crudProject/crudApp/apps.py
 create mode 100644 crudProject/crudApp/migrations/__init__.py
 create mode 100644 crudProject/crudApp/models.py
 create mode 100644 crudProject/crudApp/tests.py
 create mode 100644 crudProject/crudApp/views.py
 create mode 100644 crudProject/crudProject/__init__.py
 create mode 100644 crudProject/crudProject/__pycache__/__init__.cpython-312.pyc
 create mode 100644 crudProject/crudProject/__pycache__/settings.cpython-312.pyc
 create mode 100644 crudProject/crudProject/asgi.py
 create mode 100644 crudProject/crudProject/settings.py
 create mode 100644 crudProject/crudProject/urls.py
 create mode 100644 crudProject/crudProject/wsgi.py
 create mode 100644 crudProject/manage.py

=============================================================================
=============================================================================
=============================================================================
=============================================================================
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Etc/Universal
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Etc/Zulu
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Etc/__init__.py
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Etc/__pycache__/__init__.cpython-312.pyc
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Amsterdam
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Andorra
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Astrakhan
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Athens
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Belfast
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Belgrade
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Berlin
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Bratislava
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Brussels
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Bucharest
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Budapest
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Busingen
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Chisinau
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Copenhagen
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Dublin
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Gibraltar
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Guernsey
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Helsinki
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Isle_of_Man
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Istanbul
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Jersey
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Kaliningrad
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Kiev
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Kirov
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Kyiv
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Lisbon
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Ljubljana
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/London
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Luxembourg
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Madrid
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Malta
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Mariehamn
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Minsk
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Monaco
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Moscow
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Nicosia
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Oslo
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Paris
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Podgorica
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Prague
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Riga
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Rome
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Samara
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/San_Marino
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Sarajevo
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Saratov
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Simferopol
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Skopje
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Sofia
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Stockholm
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Tallinn
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Tirane
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Tiraspol
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Ulyanovsk
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Uzhgorod
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Vaduz
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Vatican
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Vienna
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Vilnius
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Volgograd
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Warsaw
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Zagreb
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Zaporozhye
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/Zurich
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/__init__.py
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Europe/__pycache__/__init__.cpython-312.pyc        
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Factory
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/GB
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/GB-Eire
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/GMT
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/GMT+0
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/GMT-0
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/GMT0
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Greenwich
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/HST
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Hongkong
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Iceland
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/Antananarivo
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/Chagos
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/Christmas
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/Cocos
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/Comoro
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/Kerguelen
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/Mahe
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/Maldives
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/Mauritius
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/Mayotte
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/Reunion
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/__init__.py
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Indian/__pycache__/__init__.cpython-312.pyc        
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Iran
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Israel
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Jamaica
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Japan
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Kwajalein
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Libya
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/MET
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/MST
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/MST7MDT
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Mexico/BajaNorte
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Mexico/BajaSur
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Mexico/General
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Mexico/__init__.py
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Mexico/__pycache__/__init__.cpython-312.pyc        
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/NZ
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/NZ-CHAT
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Navajo
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/PRC
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/PST8PDT
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Apia
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Auckland
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Bougainville
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Chatham
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Chuuk
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Easter
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Efate
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Enderbury
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Fakaofo
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Fiji
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Funafuti
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Galapagos
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Gambier
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Guadalcanal
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Guam
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Honolulu
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Johnston
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Kanton
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Kiritimati
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Kosrae
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Kwajalein
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Majuro
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Marquesas
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Midway
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Nauru
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Niue
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Norfolk
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Noumea
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Pago_Pago
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Palau
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Pitcairn
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Pohnpei
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Ponape
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Port_Moresby
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Rarotonga
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Saipan
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Samoa
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Tahiti
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Tarawa
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Tongatapu
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Truk
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Wake
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Wallis
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/Yap
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/__init__.py
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Pacific/__pycache__/__init__.cpython-312.pyc       
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Poland
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Portugal
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/ROC
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/ROK
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Singapore
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Turkey
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/UCT
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/Alaska
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/Aleutian
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/Arizona
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/Central
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/East-Indiana
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/Eastern
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/Hawaii
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/Indiana-Starke
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/Michigan
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/Mountain
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/Pacific
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/Samoa
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/__init__.py
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/US/__pycache__/__init__.cpython-312.pyc
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/UTC
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Universal
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/W-SU
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/WET
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/Zulu
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/__init__.py
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/__pycache__/__init__.cpython-312.pyc
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/iso3166.tab
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/leapseconds
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/tzdata.zi
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/zone.tab
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/zone1970.tab
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zoneinfo/zonenow.tab
 create mode 100644 venv-240619-1445-/Lib/site-packages/tzdata/zones
 create mode 100644 venv-240619-1445-/Scripts/Activate.ps1
 create mode 100644 venv-240619-1445-/Scripts/activate
 create mode 100644 venv-240619-1445-/Scripts/activate.bat
 create mode 100644 venv-240619-1445-/Scripts/deactivate.bat
 create mode 100644 venv-240619-1445-/Scripts/django-admin.exe
 create mode 100644 venv-240619-1445-/Scripts/pip.exe
 create mode 100644 venv-240619-1445-/Scripts/pip3.12.exe
 create mode 100644 venv-240619-1445-/Scripts/pip3.exe
 create mode 100644 venv-240619-1445-/Scripts/python.exe
 create mode 100644 venv-240619-1445-/Scripts/pythonw.exe
 create mode 100644 venv-240619-1445-/Scripts/sqlformat.exe
 create mode 100644 venv-240619-1445-/pyvenv.cfg
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (master)
$ git remote add origin https://github.com/pankaj-basnet/Django-notes-main.git
git branch -M main
git push -u origin main
Enumerating objects: 8810, done.
Counting objects: 100% (8810/8810), done.
Delta compression using up to 16 threads
Compressing objects: 100% (5612/5612), done.
Writing objects: 100% (8810/8810), 16.74 MiB | 1.46 MiB/s, done.
Total 8810 (delta 2110), reused 8810 (delta 2110), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2110/2110), done.
To https://github.com/pankaj-basnet/Django-notes-main.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (main)
$ django-admin startproject crudProject
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (main)
$ cd crudProject
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ ls -a
./  ../  crudProject/  manage.py*
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py startapp crudApp
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py check
System check identified no issues (0 silenced).
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py makemigrations
No changes detected
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 19, 2024 - 15:00:43
Django version 5.0.6, using settings 'crudProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[19/Jun/2024 15:00:51] "GET / HTTP/1.1" 200 10629
Not Found: /favicon.ico
[19/Jun/2024 15:00:51] "GET /favicon.ico HTTP/1.1" 404 2115

(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ ls -a
./  ../  crudApp/  crudProject/  db.sqlite3  manage.py*
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ which python
/d/sip-/june19-DJANGO--main-notes/venv-240619-1445-/Scripts/python
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py createsuperuser
Username (leave blank to use 'saurav'): admin   
Email address:
Password:
Password (again):
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 19, 2024 - 15:24:39
Django version 5.0.6, using settings 'crudProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[19/Jun/2024 15:24:53] "GET /admin HTTP/1.1" 301 0
[19/Jun/2024 15:24:53] "GET /admin/ HTTP/1.1" 302 0
[19/Jun/2024 15:24:53] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 4158
[19/Jun/2024 15:24:53] "GET /static/admin/css/base.css HTTP/1.1" 200 21544
[19/Jun/2024 15:24:53] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 200 3063
[19/Jun/2024 15:24:53] "GET /static/admin/css/dark_mode.css HTTP/1.1" 200 2682
[19/Jun/2024 15:24:53] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 200 2810
[19/Jun/2024 15:24:53] "GET /static/admin/css/login.css HTTP/1.1" 200 958
[19/Jun/2024 15:24:53] "GET /static/admin/css/responsive.css HTTP/1.1" 200 17905
[19/Jun/2024 15:24:53] "GET /static/admin/js/theme.js HTTP/1.1" 200 1943
[19/Jun/2024 15:25:02] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[19/Jun/2024 15:25:02] "GET /admin/ HTTP/1.1" 200 5533
[19/Jun/2024 15:25:02] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 441
[19/Jun/2024 15:25:02] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[19/Jun/2024 15:25:02] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[19/Jun/2024 15:25:05] "GET /admin/ HTTP/1.1" 200 5533
[19/Jun/2024 15:26:06] "GET /admin/ HTTP/1.1" 200 5533
[19/Jun/2024 15:26:17] "GET /admin/ HTTP/1.1" 200 5533
[19/Jun/2024 15:26:19] "GET /admin/ HTTP/1.1" 200 5533
D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\settings.py changed, reloading.
Watching for file changes with StatReloader
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1073, in _bootstrap_inner
    self.run()
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1010, in run
    self._target(*self._args, **self._kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\commands\runserver.py", line 125, in inner_run
    autoreload.raise_last_exception()
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\autoreload.py", line 87, in raise_last_exception       
    raise _exception[1]
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\__init__.py", line 394, in execute
    autoreload.check_errors(django.setup)()
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\apps\registry.py", line 91, in populate
    app_config = AppConfig.create(entry)
                 ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\apps\config.py", line 193, in create
    import_module(entry)
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1384, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1298, in _sanity_check
ValueError: Empty module name
D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\settings.py changed, reloading.
Watching for file changes with StatReloader
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1073, in _bootstrap_inner
    self.run()
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1010, in run
    self._target(*self._args, **self._kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\commands\runserver.py", line 125, in inner_run
    autoreload.raise_last_exception()
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\autoreload.py", line 87, in raise_last_exception       
    raise _exception[1]
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\__init__.py", line 394, in execute
    autoreload.check_errors(django.setup)()
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\apps\registry.py", line 91, in populate
    app_config = AppConfig.create(entry)
                 ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\apps\config.py", line 193, in create
    import_module(entry)
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1324, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'crudA'
D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\settings.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 19, 2024 - 15:26:58
Django version 5.0.6, using settings 'crudProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\settings.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 19, 2024 - 15:27:06
Django version 5.0.6, using settings 'crudProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[19/Jun/2024 15:27:16] "GET /admin/ HTTP/1.1" 200 6621
[19/Jun/2024 15:27:22] "GET /admin/crudApp/teacher/add/ HTTP/1.1" 200 10360
[19/Jun/2024 15:27:22] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:27:22] "GET /static/admin/css/forms.css HTTP/1.1" 200 9090
[19/Jun/2024 15:27:22] "GET /static/admin/js/urlify.js HTTP/1.1" 200 7887
[19/Jun/2024 15:27:22] "GET /static/admin/css/widgets.css HTTP/1.1" 200 11800
[19/Jun/2024 15:27:22] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
[19/Jun/2024 15:27:22] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 325171
[19/Jun/2024 15:27:22] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 586
[19/Jun/2024 15:27:22] "GET /static/admin/js/core.js HTTP/1.1" 200 6208
[19/Jun/2024 15:27:22] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 285314
[19/Jun/2024 15:27:22] "GET /static/admin/js/actions.js HTTP/1.1" 200 8067
[19/Jun/2024 15:27:22] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
[19/Jun/2024 15:27:22] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 9042
[19/Jun/2024 15:27:22] "GET /static/admin/js/change_form.js HTTP/1.1" 200 606
Internal Server Error: /admin/crudApp/teacher/add/
Traceback (most recent call last):
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\backends\sqlite3\base.py", line 329, in execute
    return super().execute(query, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
sqlite3.OperationalError: no such table: crudApp_teacher

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\handlers\base.py", line 197, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\contrib\admin\options.py", line 716, in wrapper
    return self.admin_site.admin_view(view)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\decorators.py", line 188, in _view_wrapper
    result = _process_exception(request, e)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\decorators.py", line 186, in _view_wrapper
    response = view_func(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\views\decorators\cache.py", line 80, in _view_wrapper        
    response = view_func(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\contrib\admin\sites.py", line 240, in inner
    return view(request, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\contrib\admin\options.py", line 1945, in add_view
    return self.changeform_view(request, None, form_url, extra_context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\decorators.py", line 48, in _wrapper
    return bound_method(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\decorators.py", line 188, in _view_wrapper
    result = _process_exception(request, e)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\decorators.py", line 186, in _view_wrapper
    response = view_func(request, *args, **kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\contrib\admin\options.py", line 1804, in changeform_view     
    return self._changeform_view(request, object_id, form_url, extra_context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\contrib\admin\options.py", line 1855, in _changeform_view    
    self.save_model(request, new_object, form, not add)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\contrib\admin\options.py", line 1259, in save_model
    obj.save()
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\models\base.py", line 822, in save
    self.save_base(
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\models\base.py", line 909, in save_base
    updated = self._save_table(
              ^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\models\base.py", line 1071, in _save_table
    results = self._do_insert(
              ^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\models\base.py", line 1112, in _do_insert
    return manager._insert(
           ^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\models\manager.py", line 87, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\models\query.py", line 1847, in _insert
    return query.get_compiler(using=using).execute_sql(returning_fields)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\models\sql\compiler.py", line 1823, in execute_sql        
    cursor.execute(sql, params)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\backends\utils.py", line 122, in execute
    return super().execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\backends\utils.py", line 79, in execute
    return self._execute_with_wrappers(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\backends\utils.py", line 92, in _execute_with_wrappers    
    return executor(sql, params, many, context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\backends\utils.py", line 100, in _execute
    with self.db.wrap_database_errors:
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\backends\utils.py", line 105, in _execute
    return self.cursor.execute(sql, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\db\backends\sqlite3\base.py", line 329, in execute
    return super().execute(query, params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django.db.utils.OperationalError: no such table: crudApp_teacher
[19/Jun/2024 15:27:32] "POST /admin/crudApp/teacher/add/ HTTP/1.1" 500 214259
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ ls -a
./  ../  crudApp/  crudProject/  db.sqlite3  manage.py*
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py check
System check identified no issues (0 silenced).
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py makemigrations
Migrations for 'crudApp':
  crudApp\migrations\0001_initial.py
    - Create model Student
    - Create model Teacher
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, crudApp, sessions
Running migrations:
  Applying crudApp.0001_initial... OK
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 19, 2024 - 15:29:09
Django version 5.0.6, using settings 'crudProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[19/Jun/2024 15:29:12] "POST /admin/crudApp/teacher/add/ HTTP/1.1" 302 0
[19/Jun/2024 15:29:12] "GET /admin/crudApp/teacher/ HTTP/1.1" 200 11187
[19/Jun/2024 15:29:12] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:29:12] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6811
[19/Jun/2024 15:29:12] "GET /static/admin/img/search.svg HTTP/1.1" 200 458
[19/Jun/2024 15:29:12] "GET /static/admin/js/filters.js HTTP/1.1" 200 978
[19/Jun/2024 15:29:13] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 200 436
[19/Jun/2024 15:29:13] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[19/Jun/2024 15:29:13] "GET /static/admin/img/sorting-icons.svg HTTP/1.1" 200 1097
[19/Jun/2024 15:29:13] "GET /static/admin/img/icon-viewlink.svg HTTP/1.1" 200 581
[19/Jun/2024 15:29:16] "GET /admin/crudApp/teacher/add/ HTTP/1.1" 200 10360
[19/Jun/2024 15:29:16] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:29:31] "POST /admin/crudApp/teacher/add/ HTTP/1.1" 302 0
[19/Jun/2024 15:29:31] "GET /admin/crudApp/teacher/ HTTP/1.1" 200 11681
[19/Jun/2024 15:29:31] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[19/Jun/2024 15:29:31] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0
[19/Jun/2024 15:29:31] "GET /static/admin/css/dark_mode.css HTTP/1.1" 304 0
[19/Jun/2024 15:29:31] "GET /static/admin/css/responsive.css HTTP/1.1" 304 0
[19/Jun/2024 15:29:31] "GET /static/admin/js/theme.js HTTP/1.1" 304 0
[19/Jun/2024 15:29:31] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:29:31] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 304 0
[19/Jun/2024 15:29:43] "GET /admin/crudApp/student/add/ HTTP/1.1" 200 9137
[19/Jun/2024 15:29:43] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1073, in _bootstrap_inner
    self.run()
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1010, in run
    self._target(*self._args, **self._kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\commands\runserver.py", line 133, in inner_run
    self.check(display_num_errors=True)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\base.py", line 486, in check
    all_issues = checks.run_checks(
                 ^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\registry.py", line 88, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\urls.py", line 14, in check_url_config
    return check_resolver(resolver)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\urls.py", line 24, in check_resolver
    return check_method()
           ^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 519, in check
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\urls.py", line 22, in <module>
    path("", views.home)
             ^^^^^
NameError: name 'views' is not defined
D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1073, in _bootstrap_inner
    self.run()
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1010, in run
    self._target(*self._args, **self._kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\commands\runserver.py", line 133, in inner_run
    self.check(display_num_errors=True)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\base.py", line 486, in check
    all_issues = checks.run_checks(
                 ^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\registry.py", line 88, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\urls.py", line 14, in check_url_config
    return check_resolver(resolver)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\urls.py", line 24, in check_resolver
    return check_method()
           ^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 519, in check
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\urls.py", line 19, in <module>
    from app import views
ModuleNotFoundError: No module named 'app'
D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1073, in _bootstrap_inner
    self.run()
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1010, in run
    self._target(*self._args, **self._kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\commands\runserver.py", line 133, in inner_run
    self.check(display_num_errors=True)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\base.py", line 486, in check
    all_issues = checks.run_checks(
                 ^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\registry.py", line 88, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\urls.py", line 14, in check_url_config
    return check_resolver(resolver)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\urls.py", line 24, in check_resolver
    return check_method()
           ^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 519, in check
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\urls.py", line 19, in <module>
    from crud import views
ModuleNotFoundError: No module named 'crud'

(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1073, in _bootstrap_inner
    self.run()
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1010, in run
    self._target(*self._args, **self._kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\commands\runserver.py", line 133, in inner_run
    self.check(display_num_errors=True)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\base.py", line 486, in check
    all_issues = checks.run_checks(
                 ^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\registry.py", line 88, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\urls.py", line 14, in check_url_config
    return check_resolver(resolver)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\urls.py", line 24, in check_resolver
    return check_method()
           ^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 519, in check
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\urls.py", line 24, in <module>
    path("", views.home)
             ^^^^^^^^^^
AttributeError: module 'crudApp.views' has no attribute 'home'
D:\sip-\june19-DJANGO--main-notes\crudProject\crudApp\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 19, 2024 - 15:34:43
Django version 5.0.6, using settings 'crudProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[19/Jun/2024 15:35:08] "GET / HTTP/1.1" 200 245
D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\settings.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 19, 2024 - 15:42:17
Django version 5.0.6, using settings 'crudProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1073, in _bootstrap_inner
    self.run()
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1010, in run
    self._target(*self._args, **self._kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\commands\runserver.py", line 133, in inner_run
    self.check(display_num_errors=True)
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\management\base.py", line 486, in check
    all_issues = checks.run_checks(
                 ^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\registry.py", line 88, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\urls.py", line 14, in check_url_config
    return check_resolver(resolver)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\core\checks\urls.py", line 24, in check_resolver
    return check_method()
           ^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 519, in check
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 738, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\utils\functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ^^^^^^^^^^^^^^^^^^^
  File "D:\sip-\june19-DJANGO--main-notes\venv-240619-1445-\Lib\site-packages\django\urls\resolvers.py", line 731, in urlconf_module
    return import_module(self.urlconf_name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\saurav\AppData\Local\Programs\Python\Python312\Lib\importlib\__init__.py", line 90, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 995, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\urls.py", line 25, in <module>
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
       ^^^^^^
NameError: name 'static' is not defined
D:\sip-\june19-DJANGO--main-notes\crudProject\crudProject\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 19, 2024 - 15:44:11
Django version 5.0.6, using settings 'crudProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[19/Jun/2024 15:44:18] "GET /admin/crudApp/student/add/ HTTP/1.1" 200 9137
[19/Jun/2024 15:44:18] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/css/dark_mode.css HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/js/core.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/js/jquery.init.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/css/forms.css HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/css/responsive.css HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/js/urlify.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/js/prepopulate.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/js/actions.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/css/widgets.css HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:18] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:44:19] "GET /static/admin/js/theme.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:19] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:19] "GET /static/admin/js/change_form.js HTTP/1.1" 304 0
[19/Jun/2024 15:44:19] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 304 0
[19/Jun/2024 15:45:20] "POST /admin/crudApp/student/add/ HTTP/1.1" 302 0
[19/Jun/2024 15:45:20] "GET /admin/crudApp/student/ HTTP/1.1" 200 9240
[19/Jun/2024 15:45:20] "GET /static/admin/css/changelists.css HTTP/1.1" 304 0
[19/Jun/2024 15:45:20] "GET /static/admin/js/filters.js HTTP/1.1" 304 0
[19/Jun/2024 15:45:20] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:45:20] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 304 0
[19/Jun/2024 15:45:20] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 304 0
[19/Jun/2024 15:45:27] "GET /admin/crudApp/student/add/ HTTP/1.1" 200 9137
[19/Jun/2024 15:45:27] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:45:38] "POST /admin/crudApp/student/add/ HTTP/1.1" 302 0
[19/Jun/2024 15:45:38] "GET /admin/crudApp/student/ HTTP/1.1" 200 9528
[19/Jun/2024 15:45:38] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:45:42] "GET /admin/crudApp/teacher/ HTTP/1.1" 200 11481
[19/Jun/2024 15:45:42] "GET /static/admin/img/search.svg HTTP/1.1" 304 0
[19/Jun/2024 15:45:42] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:45:42] "GET /static/admin/img/sorting-icons.svg HTTP/1.1" 304 0
[19/Jun/2024 15:45:42] "GET /static/admin/img/icon-viewlink.svg HTTP/1.1" 304 0
[19/Jun/2024 15:45:47] "GET /admin/crudApp/student/ HTTP/1.1" 200 9315
[19/Jun/2024 15:45:47] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:45:49] "GET /admin/crudApp/teacher/ HTTP/1.1" 200 11481
[19/Jun/2024 15:45:49] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:45:51] "GET /admin/crudApp/student/ HTTP/1.1" 200 9315
[19/Jun/2024 15:45:51] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:45:54] "GET /admin/crudApp/student/2/change/ HTTP/1.1" 200 9536
[19/Jun/2024 15:45:54] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:46:01] "GET /admin/crudApp/teacher/ HTTP/1.1" 200 11481
[19/Jun/2024 15:46:01] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:46:03] "GET /admin/crudApp/student/ HTTP/1.1" 200 9315
[19/Jun/2024 15:46:03] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:46:05] "GET /admin/crudApp/student/1/change/ HTTP/1.1" 200 9499
[19/Jun/2024 15:46:05] "GET /admin/jsi18n/ HTTP/1.1" 200 3342
[19/Jun/2024 15:46:26] "GET / HTTP/1.1" 200 245
[19/Jun/2024 15:46:27] "GET / HTTP/1.1" 200 245
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 19, 2024 - 15:46:35
Django version 5.0.6, using settings 'crudProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

[19/Jun/2024 15:46:38] "GET / HTTP/1.1" 200 245
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ ls -a
./  ../  crudApp/  crudProject/  db.sqlite3  manage.py*  media/
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ which python
/d/sip-/june19-DJANGO--main-notes/venv-240619-1445-/Scripts/python
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes/crudProject (main)
$ cd ../
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (main)
$ ls -a
./     crudProject/                                                             requirements.txt
../    extra---imp---notes---for--JUNE19-Django--MAIN-NOTES---crudProject--.md  r---requirements-txt-----on-june19---done-.txt
.git/  imp-notes---django--from-june-19-.md                                     venv-240619-1445-/
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (main)
$ git add .
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (main)
$ git commit -am "added media setting and media folder---added admin register decorator----two models"
[main 68e91d5] added media setting and media folder---added admin register decorator----two models
 22 files changed, 91 insertions(+), 1 deletion(-)
 create mode 100644 crudProject/crudApp/__pycache__/__init__.cpython-312.pyc
 create mode 100644 crudProject/crudApp/__pycache__/admin.cpython-312.pyc
 create mode 100644 crudProject/crudApp/__pycache__/apps.cpython-312.pyc
 create mode 100644 crudProject/crudApp/__pycache__/models.cpython-312.pyc
 create mode 100644 crudProject/crudApp/__pycache__/views.cpython-312.pyc
 create mode 100644 crudProject/crudApp/migrations/0001_initial.py
 create mode 100644 crudProject/crudApp/migrations/__pycache__/0001_initial.cpython-312.pyc
 create mode 100644 crudProject/crudApp/migrations/__pycache__/__init__.cpython-312.pyc
 create mode 100644 crudProject/crudApp/templates/home.html
 create mode 100644 crudProject/crudProject/__pycache__/urls.cpython-312.pyc
 create mode 100644 crudProject/crudProject/__pycache__/wsgi.cpython-312.pyc
 create mode 100644 crudProject/db.sqlite3
 create mode 100644 crudProject/media/image/coffee_web.jpg
 create mode 100644 crudProject/media/image/pexels-anjana-c-169994-674010.jpg
 create mode 100644 extra---imp---notes---for--JUNE19-Django--MAIN-NOTES---crudProject--.md
 create mode 100644 imp-notes---django--from-june-19-.md
(venv-240619-1445-) 
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (main)
$ git push -u origin main
Enumerating objects: 53, done.
Counting objects: 100% (53/53), done.
Delta compression using up to 16 threads
Compressing objects: 100% (49/49), done.
Writing objects: 100% (52/52), 2.39 MiB | 912.00 KiB/s, done.
Total 52 (delta 10), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (10/10), done.
To https://github.com/pankaj-basnet/Django-notes-main.git
   bb18ebf..68e91d5  main -> main
branch 'main' set up to track 'origin/main'.
(venv-240619-1445-)
saurav@LAPTOP-JS10JJ6V MINGW64 /d/sip-/june19-DJANGO--main-notes (main
=============================================================================
=============================================================================
=============================================================================
=============================================================================
=============================================================================
=============================================================================
=============================================================================
=============================================================================