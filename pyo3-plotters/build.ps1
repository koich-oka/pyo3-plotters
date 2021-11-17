 $env:VIRTUAL_ENV =  (Get-Item ..\venv\).FullName
 ..\venv\Scripts\maturin.exe develop
