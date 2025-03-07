cmake_minimum_required(VERSION 3.28)
project(lab10)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_PREFIX_PATH "/Users/mihaiadomnitei/Qt/6.7.0/macos/lib/cmake")

find_package(Qt6 COMPONENTS
        Core
        Gui
        Widgets
        REQUIRED)

add_executable(lab10
        include/Console.hpp
        include/Medicament.hpp
        include/Repository.hpp
        include/Test.hpp
        include/Service.hpp
        include/Undo.hpp
        include/Validator.hpp
        src/Console.cpp
        src/ConsoleRecipe.cpp
        src/main.cpp
        src/Medicament.cpp
        src/Repository.cpp
        src/Service.cpp
        src/Test.cpp
        src/Undo.cpp
        src/Validator.cpp
        include/Gui.hpp
        src/Gui.cpp
        include/GuiRecipe.hpp
        src/GuiRecipe.cpp
        include/TableModel.hpp
        src/TableModel.cpp
        include/RecipeDrawing.hpp
        include/Observer.hpp
)
target_link_libraries(lab10
        Qt::Core
        Qt::Gui
        Qt::Widgets
)

target_include_directories(lab10 PUBLIC include)
target_include_directories(lab10 PUBLIC database)
