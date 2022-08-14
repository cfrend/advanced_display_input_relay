. "$PSScriptRoot\VirtualDesktop\VirtualDesktop.ps1"

#Check if there are 5 desktops and if there are not, make them one by one.
$desktopCount = Get-DesktopCount
If ($desktopCount -lt 5){
	New-Desktop
	$desktopCount = Get-DesktopCount
	If ($desktopCount -lt 5){
		New-Desktop
		$desktopCount = Get-DesktopCount
		If ($desktopCount -lt 5){
			New-Desktop
			$desktopCount = Get-DesktopCount
			If ($desktopCount -lt 5){
				New-Desktop
				$desktopCount = Get-DesktopCount
			}
		}
	}
}

#region Desktop 1 setup
$desktop1 = Get-Desktop -Index 0
Switch-Desktop -Desktop $desktop1
#Welcome Collectome Screen
C:\api\automation\Scripts\python.exe C:\api\ps1_scripts\VIPTourContentSetup01\desktop01Content.py
Sleep 5
#endregion

#region Desktop 2 setup
$desktop2 = Get-Desktop -Index 1
Switch-Desktop -Desktop $desktop2
#Voice controlled content setup
C:\api\automation\Scripts\python.exe C:\api\ps1_scripts\VIPTourContentSetup01\desktop02Content.py
Sleep 5
#endregion

#region Desktop 3 setup
$desktop3 = Get-Desktop -Index 2
Switch-Desktop -Desktop $desktop3
C:\api\automation\Scripts\python.exe C:\api\ps1_scripts\VIPTourContentSetup01\desktop03Content.py
Sleep 10
#endregion

#region Desktop 4 setup
$desktop4 = Get-Desktop -Index 3
Switch-Desktop -Desktop $desktop4
C:\api\automation\Scripts\python.exe C:\api\ps1_scripts\VIPTourContentSetup01\desktop04Content.py
Sleep 5
#endregion

#region Desktop 5 setup
$desktop5 = Get-Desktop -Index 4
Switch-Desktop -Desktop $desktop5
C:\api\automation\Scripts\python.exe C:\api\ps1_scripts\VIPTourContentSetup01\desktop05Content.py
Sleep 5
#endregion
