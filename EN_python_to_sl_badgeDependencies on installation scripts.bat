@chcp 65001 >nul
@echo off
echo " ___    ___  ___  ___   _______    ________   ___   ___  ___          ________   ________   ___   ___  ___     ";
echo "|\  \  /  /||\  \|\  \ |\  ___ \  |\   __  \ |\  \ |\  \|\  \        |\   __  \ |\   __  \ |\  \ |\  \|\  \    ";
echo "\ \  \/  / /\ \  \\\  \\ \   __/| \ \  \|\  \\ \  \\ \  \\\  \       \ \  \|\ /_\ \  \|\  \\ \  \\ \  \\\  \   ";
echo " \ \    / /  \ \  \\\  \\ \  \_|/__\ \  \\\  \\ \  \\ \  \\\  \       \ \   __  \\ \  \\\  \\ \  \\ \  \\\  \  ";
echo "  /     \/    \ \  \\\  \\ \  \_|\ \\ \  \\\  \\ \  \\ \  \\\  \       \ \  \|\  \\ \  \\\  \\ \  \\ \  \\\  \ ";
echo " /  /\   \     \ \_______\\ \_______\\ \_____  \\ \__\\ \_______\       \ \_______\\ \_____  \\ \__\\ \_______\";
echo "/__/ /\ __\     \|_______| \|_______| \|___| \__\\|__| \|_______|        \|_______| \|___| \__\\|__| \|_______|";
echo "|__|/ \|__|                                 \|__|                                         \|__|                ";
echo "                                                                                                               ";
echo "                                                                                                               ";
echo "   ________   ________   _________        ________  ________   ________     ";
echo "  |\   __  \ |\   __  \ |\___   ___\     |\  _____\|\   __  \ |\   __  \    ";
echo "  \ \  \|\ /_\ \  \|\  \\|___ \  \_|     \ \  \__/ \ \  \|\  \\ \  \|\  \   ";
echo "   \ \   __  \\ \   __  \    \ \  \       \ \   __\ \ \  \\\  \\ \   _  _\  ";
echo " ___\ \  \|\  \\ \  \ \  \    \ \  \       \ \  \_|  \ \  \\\  \\ \  \\  \| ";
echo "|\__\\ \_______\\ \__\ \__\    \ \__\       \ \__\    \ \_______\\ \__\\ _\ ";
echo "\|__| \|_______| \|__|\|__|     \|__|        \|__|     \|_______| \|__|\|__|";
echo "                                                                            ";
echo "                                                                            ";
echo "                                                                            ";
echo "   _______        _________        _______ _       ________________     _______ _           ______  _______ ______  _______ _______ ";
echo "  (  ____ |\     /\__   __|\     /(  ___  ( (    /|\__   __(  ___  )   (  ____ ( \         (  ___ \(  ___  (  __  \(  ____ (  ____ \";
echo "  | (    )( \   / )  ) (  | )   ( | (   ) |  \  ( |   ) (  | (   ) |   | (    \| (         | (   ) | (   ) | (  \  | (    \| (    \/";
echo "  | (____)|\ (_) /   | |  | (___) | |   | |   \ | |   | |  | |   | |   | (_____| |         | (__/ /| (___) | |   ) | |     | (__    ";
echo "  |  _____) \   /    | |  |  ___  | |   | | (\ \) |   | |  | |   | |   (_____  | |         |  __ ( |  ___  | |   | | | ____|  __)   ";
echo "  | (        ) (     | |  | (   ) | |   | | | \   |   | |  | |   | |         ) | |         | (  \ \| (   ) | |   ) | | \_  | (      ";
echo "  | )        | |     | |  | )   ( | (___) | )  \  |   | |  | (___) |   /\____) | (____/\   | )___) | )   ( | (__/  | (___) | (____/\";
echo "  |/         \_/     )_(  |/     \(_______|/    )_____)_(  (___________\_______(___________|/ \___/|/     \(______/(_______(_______/";
echo "                                                 (_____)          (_____)             (_____)                                       ";
echo —— Give your child a star! Thank you!
echo —— Welcome to visit https://bqiu.top my blog
echo —— Please follow me! Thank you!
echo —— My Github homepage: https://github.com/wsxqyy
echo Please make sure you have the appropriate Python and pip installed on your computer; otherwise, this script will not work. This .bat file is only for installing python_to_sl_badge and may not be suitable for all py version programs.
echo Please press Y to proceed, N to exit
set /p choice=
if /i "%choice%"=="Y" (
    echo Starting installation...
    pip install flask
    echo Installation 20% complete.
    pip install mysql-connector-python
    echo Installation 50% complete.
    echo Starting to install other dependencies
    pip install python-dotenv
    echo Installation complete!
) else if /i "%choice%"=="N" (
    echo You have chosen to exit.
    goto :eof
) else (
    echo Invalid input, please try again.
)
echo Press any key to exit. Please open the py script and then visit 127.0.0.1:5000 in your browser to use it.
pause >nul