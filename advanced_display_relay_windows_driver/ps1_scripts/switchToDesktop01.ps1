. "$PSScriptRoot\VirtualDesktop\VirtualDesktop.ps1"

$desktopCount = Get-DesktopCount

#Check if there are 5 desktops and if there are not, make them one by one.
# If ($desktopCount -lt 5){
	# New-Desktop
	# $desktopCount = Get-DesktopCount
	# If ($desktopCount -lt 5){
		# New-Desktop
		# $desktopCount = Get-DesktopCount
		# If ($desktopCount -lt 5){
			# New-Desktop
			# $desktopCount = Get-DesktopCount
			# If ($desktopCount -lt 5){
				# New-Desktop
				# $desktopCount = Get-DesktopCount
			# }
		# }
	# }
# }

$desktop1 = Get-Desktop -Index 0

Switch-Desktop -Desktop $desktop1