#contents of install_numpy.ps1

function InstallNumpy(){
 
    if (-not(Test-Path "c:\tmp\*.whl")) {
        Write-Host "numpy has not been compiled yet. Starting Long process..."
        Write-Host "pip wheel --wheel-dir=c:\tmp\ numpy"
        iex "cmd /E:ON /V:ON /C .\\appveyor\\run_with_env.cmd pip wheel --wheel-dir=c:\\tmp numpy"
    } else {
        Write-Host "numpy has already been compiled."
        Get-ChildItem "C:\tmp"
    }
}

InstallNumpy
