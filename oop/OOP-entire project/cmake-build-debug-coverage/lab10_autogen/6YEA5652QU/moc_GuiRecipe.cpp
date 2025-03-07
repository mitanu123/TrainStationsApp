/****************************************************************************
** Meta object code from reading C++ file 'GuiRecipe.hpp'
**
** Created by: The Qt Meta Object Compiler version 68 (Qt 6.7.0)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../include/GuiRecipe.hpp"
#include <QtCore/qmetatype.h>

#include <QtCore/qtmochelpers.h>

#include <memory>


#include <QtCore/qxptype_traits.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'GuiRecipe.hpp' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 68
#error "This file was generated using the moc from 6.7.0. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif

QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
QT_WARNING_DISABLE_GCC("-Wuseless-cast")
namespace {

#ifdef QT_MOC_HAS_STRINGDATA
struct qt_meta_stringdata_CLASSGUIRecipeENDCLASS_t {};
constexpr auto qt_meta_stringdata_CLASSGUIRecipeENDCLASS = QtMocHelpers::stringData(
    "GUIRecipe",
    "addRecipe",
    "",
    "deleteAllRecipes",
    "populateRandomRecipe",
    "exportToHTML",
    "exportToCSV",
    "printRecipe"
);
#else  // !QT_MOC_HAS_STRINGDATA
#error "qtmochelpers.h not found or too old."
#endif // !QT_MOC_HAS_STRINGDATA
} // unnamed namespace

Q_CONSTINIT static const uint qt_meta_data_CLASSGUIRecipeENDCLASS[] = {

 // content:
      12,       // revision
       0,       // classname
       0,    0, // classinfo
       6,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags, initial metatype offsets
       1,    0,   50,    2, 0x0a,    1 /* Public */,
       3,    0,   51,    2, 0x0a,    2 /* Public */,
       4,    0,   52,    2, 0x0a,    3 /* Public */,
       5,    0,   53,    2, 0x0a,    4 /* Public */,
       6,    0,   54,    2, 0x0a,    5 /* Public */,
       7,    0,   55,    2, 0x0a,    6 /* Public */,

 // slots: parameters
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

Q_CONSTINIT const QMetaObject GUIRecipe::staticMetaObject = { {
    QMetaObject::SuperData::link<QWidget::staticMetaObject>(),
    qt_meta_stringdata_CLASSGUIRecipeENDCLASS.offsetsAndSizes,
    qt_meta_data_CLASSGUIRecipeENDCLASS,
    qt_static_metacall,
    nullptr,
    qt_incomplete_metaTypeArray<qt_meta_stringdata_CLASSGUIRecipeENDCLASS_t,
        // Q_OBJECT / Q_GADGET
        QtPrivate::TypeAndForceComplete<GUIRecipe, std::true_type>,
        // method 'addRecipe'
        QtPrivate::TypeAndForceComplete<void, std::false_type>,
        // method 'deleteAllRecipes'
        QtPrivate::TypeAndForceComplete<void, std::false_type>,
        // method 'populateRandomRecipe'
        QtPrivate::TypeAndForceComplete<void, std::false_type>,
        // method 'exportToHTML'
        QtPrivate::TypeAndForceComplete<void, std::false_type>,
        // method 'exportToCSV'
        QtPrivate::TypeAndForceComplete<void, std::false_type>,
        // method 'printRecipe'
        QtPrivate::TypeAndForceComplete<void, std::false_type>
    >,
    nullptr
} };

void GUIRecipe::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<GUIRecipe *>(_o);
        (void)_t;
        switch (_id) {
        case 0: _t->addRecipe(); break;
        case 1: _t->deleteAllRecipes(); break;
        case 2: _t->populateRandomRecipe(); break;
        case 3: _t->exportToHTML(); break;
        case 4: _t->exportToCSV(); break;
        case 5: _t->printRecipe(); break;
        default: ;
        }
    }
    (void)_a;
}

const QMetaObject *GUIRecipe::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *GUIRecipe::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_CLASSGUIRecipeENDCLASS.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int GUIRecipe::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 6)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 6;
    }
    return _id;
}
QT_WARNING_POP
