# <h1 style="text-align:center; font-size:360%; font-family:verdana;color:#4A3E76;"><em>TEST</em></h1>

# These tutorials are watched from [**_CodeWithHarry_**](https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww "Clike here to checkout his channel") YouTube channel from [**_Pyton Playlist_**](https://youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME "Clike here to check out his Python tutorials Playlist")

---

---

---

---

---

## **_1.) tutorial_1 of C/C++_**

### [**_Click me_**](tutorial_1.cpp "Clike here to see full file") to see full file of tutorial_1

```C++
// Date 24-05-2021
#include <iostream>
int main()
{
    std::cout << "hello";
    return 0;
}

```

---

---

## **_2.) tutorial_3 of C/C++_**

### [**_Click me_**](tutorial_3.cpp "Clike here to see full file") to see full file of tutorial_3

```C++
// Date 24-05-2021
#include <iostream>
using namespace std;
int main()
{
    // This is a Single line comment
    //todo This is a Single line comment
    //* This is a Single line comment
    //? This is a Single line comment
    //! This is a Single line comment

    // The down part is a variable
    int integer_variable = 20;
    // The upper part is a variable

    cout << "hello" << integer_variable + 20;
    return 0;
    /*
    This is a Multi line comment
    You can write here
    You can write here
    You can write here
    You can write here
    */
}

```

---

---

## **_3.) tutorial_4_1 of C/C++_**

### [**_Click me_**](tutorial_4_1.cpp "Clike here to see full file") to see full file of tutorial_4_1

```C++
// Date 24-05-2021
#include <iostream>
using namespace std;
int main()
{
    //? int a = 4;
    //? int b = 5;
    int a = 4, b = 5;
    float pi = 3.1428571428571428571428571428571;
    char character = '@';
    cout << "This is tutorial 4.\nHere the value of a is " << a << ".\nThe value of b is " << b << ".\nThe value of Pi is " << pi;
    cout << "\nCharacter is " << character;
    return 0;
}
```

---

---

## **_4.) tutorial_4_2 of C/C++_**

### [**_Click me_**](tutorial_4_2.cpp "Clike here to see full file") to see full file of tutorial_4_2

```C++
// Date 24-05-2021
#include <iostream>
using namespace std;

int a_global_variable = 9;

void function_1()
{
    bool is_true_or_not_1 = true;
    bool is_true_or_not_2 = false;
    int local_variable = 78;
    cout << "\n\n\n\n\nFunction_1\'s local variable is " << local_variable;
    cout << "\nGlobal variable is " << a_global_variable;
    cout << "\nValue of True is " << is_true_or_not_1;
    cout << "\nValue of False is " << is_true_or_not_2;
}
int main()
{
    cout << "\n\n\nGlobal variable is " << a_global_variable;
    a_global_variable = 45;
    cout << "\nGlobal variable after change is " << a_global_variable;

    //* The below line will throw an Error
    //? cout << "\nOther Function local variable is " << local_variable;
    //* The above line will throw an Error
    function_1();

    return 0;
}
```

---

---

## **_5.) tutorial_5 of C/C++_**

### [**_Click me_**](tutorial_5.cpp "Clike here to see full file") to see full file of tutorial_5

```C++
// Date 25-05-2021

#include <iostream>
using namespace std;

int main()
{
    int variable_1, variable_2;
    //* << is called Insertion operator
    cout << "Enter the value 1 to add:\n";
    //* << is called Insertion operator
    //* >> is called Extration operator
    cin >> variable_1;
    //* >> is called Extration operator

    //* << is called Insertion operator
    cout << "Enter the value 2 to add:\n";
    //* << is called Insertion operator
    //* >> is called Extration operator
    cin >> variable_2;
    //* >> is called Extration operator

    cout << "Sum of your values is: " << variable_1 + variable_2;

    return 0;
}

```

---

---

## **_6.) tutorial_6_1 of C/C++_**

### [**_Click me_**](tutorial_6_1.cpp "Clike here to see full file") to see full file of tutorial_6_1

```C++
// Date 25-05-2021

#include <iostream>
#include "tutorial_6_1__functions__.cpp"

//* The below line of code will produce an error if func1.cpp is not precente in the current directory
// #include "func1.cpp"
//* The above line of code will produce an error if func1.cpp is not precente in the current directory

using namespace std;

int main()
{
    cout << "Header files in C++";
    return 0;
}

```

---

---

## **_7.) tutorial_6_2_0 of C/C++_**

### [**_Click me_**](tutorial_6_2_0.cpp "Clike here to see full file") to see full file of tutorial_6_2_0

```C++
// Date 25-05-2021

#include <iostream>
using namespace std;

int main()
{
    // int num_1 = 2, num_2 = 4;
    int num_1, num_2;

    cout << "Please Enter the value of num_1" << endl;
    cin >> num_1;
    cout << "Please Enter the value of num_2" << endl;
    cin >> num_2;
    cout << endl;

    cout << "Operators in C++" << endl;
    cout << "Following are the types of C++ Operators" << endl;

    cout << ">>>> Arithmatic Operators in C++" << endl;
    cout << ">>>>>>>> The value of " << num_1 << " + " << num_2 << " is " << num_1 + num_2 << endl;
    cout << ">>>>>>>> The value of " << num_1 << " - " << num_2 << " is " << num_1 - num_2 << endl;
    cout << ">>>>>>>> The value of " << num_1 << " * " << num_2 << " is " << num_1 * num_2 << endl;
    cout << ">>>>>>>> The value of " << num_1 << " / " << num_2 << " is " << num_1 / num_2 << endl;
    cout << ">>>>>>>> The value of " << num_1 << " \% " << num_2 << " is " << num_1 % num_2 << endl;
    cout << ">>>>>>>> The value of " << num_1 << "++  is " << num_1++ << endl;
    //* Due to above line of code value of num_1 will become num_1 + 1
    cout << ">>>>>>>> The value of " << num_1 << "--  is " << num_1-- << endl;
    //* Due to above line of code value of num_1 will become num_1 - 1
    cout << ">>>>>>>> The value of ++" << num_1 << "  is " << ++num_1 << endl;
    //* Due to above line of code value of num_1 will become 1 + num_1
    cout << ">>>>>>>> The value of --" << num_1 << "  is " << --num_1 << endl;
    //* Due to above line of code value of num_1 will become 1 - num_1

    cout << ">>>> Assignment Operators in C++" << endl;
    cout << ">>>>>>>> In C++ Assignment Operators are used to assign values to any variable." << endl;
    cout << ">>>>>>>> Such as:" << endl;
    cout << ">>>>>>>> int x = 1;" << endl;
    cout << ">>>>>>>> char y = 'S';" << endl;
    cout << ">>>>>>>> Here \'=\' is an Assignment Operator." << endl;
    //* These operators are used to assign values to any variable
    int x = 1;
    char y = 'S';

    cout << ">>>> Comparision Operators in C++" << endl;
    cout << ">>>>>>>> The value of " << num_1 << " == " << num_2 << " is " << (num_1 == num_2) << endl;
    cout << ">>>>>>>> The value of " << num_1 << " != " << num_2 << " is " << (num_1 != num_2) << endl;
    cout << ">>>>>>>> The value of " << num_1 << " > " << num_2 << " is " << (num_1 > num_2) << endl;
    cout << ">>>>>>>> The value of " << num_1 << " < " << num_2 << " is " << (num_1 < num_2) << endl;
    cout << ">>>>>>>> The value of " << num_1 << " >= " << num_2 << " is " << (num_1 >= num_2) << endl;
    cout << ">>>>>>>> The value of " << num_1 << " <= " << num_2 << " is " << (num_1 <= num_2) << endl;

    cout << ">>>> Logical Operators" << endl;
    cout << ">>>>>>>> The value of Logical's AND operator i.e. ((" << num_1 << " == " << num_2 << ")"
         << " && (" << num_1 << " <= " << num_2 << "))"
         << " is " << ((num_1 == num_2) && (num_1 <= num_2)) << endl;
    cout << ">>>>>>>> The value of Logical's OR operator i.e. ((" << num_1 << " == " << num_2 << ")"
         << " || (" << num_1 << " <= " << num_2 << "))"
         << " is " << ((num_1 == num_2) || (num_1 <= num_2)) << endl;
    cout << ">>>>>>>> The value of Logical's NOT operator i.e. (!(" << num_1 << " == " << num_2 << ")) is " << (!(num_1 == num_2)) << endl;

    cout << ">>>> Bitwise Operators" << endl;
    cout << ">>>>>>>> The value of Bitwise's AND \'&\' operator i.e. (" << num_1 << " & " << num_2 << ") is " << (num_1 & num_2) << endl;
    cout << ">>>>>>>> The value of Bitwise's OR \'|\' operator i.e. (" << num_1 << " | " << num_2 << ") is " << (num_1 | num_2) << endl;
    cout << ">>>>>>>> The value of Bitwise's NOT \'~\' operator i.e. (~" << num_1 << ") is " << (~num_1) << " and (~" << num_2 << ") is " << (~num_2) << endl;
    cout << ">>>>>>>> The value of Bitwise's XOR \'^\' operator i.e. (" << num_1 << " ^ " << num_2 << ") is " << (num_1 ^ num_2) << endl;
    cout << ">>>>>>>> The value of Bitwise's Left Shift \'<<\' operator i.e. (" << num_1 << " << " << num_2 << ") is " << (num_1 << num_2) << endl;
    cout << ">>>>>>>> The value of Bitwise's Right Shift \'>>\' operator i.e. (" << num_1 << " >> " << num_2 << ") is " << (num_1 >> num_2) << endl;

    return 0;
}

```

---

---

## **_8.) tutorial_6_2_1 of C/C++_**

### [**_Click me_**](tutorial_6_2_1.cpp "Clike here to see full file") to see full file of tutorial_6_2_1

```C++
// Date 25-05-2021

#include <iostream>
using namespace std;

int main()
{
    // int num_1 = 2, num_2 = 4;
    int num_1, num_2;

    cout << "Please Enter the value of num_1" << endl;
    cin >> num_1;
    cout << "Please Enter the value of num_2" << endl;
    cin >> num_2;
    cout << endl;

    cout << "Operators in C++" << endl;
    cout << "Following are the types of C++ Operators" << endl;

    cout << ">>>> Arithmatic Operators in C++" << endl;
    cout << ">>>>>>>> The value of " << num_1 << " + " << num_2 << " is " << num_1 + num_2 << endl;
    cout << ">>>>>>>> The value of " << num_1 << " - " << num_2 << " is " << num_1 - num_2 << endl;
    cout << ">>>>>>>> The value of " << num_1 << " * " << num_2 << " is " << num_1 * num_2 << endl;
    cout << ">>>>>>>> The value of " << num_1 << " / " << num_2 << " is " << num_1 / num_2 << endl;
    cout << ">>>>>>>> The value of " << num_1 << " \% " << num_2 << " is " << num_1 % num_2 << endl;
    cout << ">>>>>>>> The value of " << num_1 << "++  is " << num_1++ << endl;
    //* Due to above line of code value of num_1 will become num_1 + 1
    cout << ">>>>>>>> The value of " << num_1 << "--  is " << num_1-- << endl;
    //* Due to above line of code value of num_1 will become num_1 - 1
    cout << ">>>>>>>> The value of ++" << num_1 << "  is " << ++num_1 << endl;
    //* Due to above line of code value of num_1 will become 1 + num_1
    cout << ">>>>>>>> The value of --" << num_1 << "  is " << --num_1 << endl
         << endl;
    //* Due to above line of code value of num_1 will become 1 - num_1

    return 0;
}

```

---

---

## **_9.) tutorial_6_2_2 of C/C++_**

### [**_Click me_**](tutorial_6_2_2.cpp "Clike here to see full file") to see full file of tutorial_6_2_2

```C++
// Date 25-05-2021

#include <iostream>
using namespace std;

int main()
{

    cout << "Operators in C++" << endl;
    cout << "Following are the types of C++ Operators" << endl;

    cout << ">>>> Assignment Operators in C++" << endl;
    cout << ">>>>>>>> In C++ Assignment Operators are used to assign values to any variable." << endl;
    cout << ">>>>>>>> Such as:" << endl;
    cout << ">>>>>>>> int x = 1;" << endl;
    cout << ">>>>>>>> char y = 'S';" << endl;
    cout << ">>>>>>>> Here \'=\' is an Assignment Operator." << endl;
    //* These operators are used to assign values to any variable
    int x = 1;
    char y = 'S';
    return 0;
}

```

---

---

## **_10.) tutorial_6_2_3 of C/C++_**

### [**_Click me_**](tutorial_6_2_3.cpp "Clike here to see full file") to see full file of tutorial_6_2_3

```C++
// Date 25-05-2021

#include <iostream>
using namespace std;

int main()
{
    int num_1, num_2;

    cout << "Please Enter the value of num_1" << endl;
    cin >> num_1;
    cout << "Please Enter the value of num_2" << endl;
    cin >> num_2;
    cout << endl;

    cout << "Operators in C++" << endl;
    cout << "Following are the types of C++ Operators" << endl;

    cout << ">>>> Comparision Operators in C++" << endl;
    cout << ">>>>>>>> The value of " << num_1 << " == " << num_2 << " is " << (num_1 == num_2) << endl;
    cout << ">>>>>>>> The value of " << num_1 << " != " << num_2 << " is " << (num_1 != num_2) << endl;
    cout << ">>>>>>>> The value of " << num_1 << " > " << num_2 << " is " << (num_1 > num_2) << endl;
    cout << ">>>>>>>> The value of " << num_1 << " < " << num_2 << " is " << (num_1 < num_2) << endl;
    cout << ">>>>>>>> The value of " << num_1 << " >= " << num_2 << " is " << (num_1 >= num_2) << endl;
    cout << ">>>>>>>> The value of " << num_1 << " <= " << num_2 << " is " << (num_1 <= num_2) << endl;
    return 0;
}

```

---

---

## **_11.) tutorial_6_2_4 of C/C++_**

### [**_Click me_**](tutorial_6_2_4.cpp "Clike here to see full file") to see full file of tutorial_6_2_4

```C++
// Date 25-05-2021

#include <iostream>
using namespace std;

int main()
{
    int num_1, num_2;

    cout << "Please Enter the value of num_1" << endl;
    cin >> num_1;
    cout << "Please Enter the value of num_2" << endl;
    cin >> num_2;
    cout << endl;

    cout << "Operators in C++" << endl;
    cout << "Following are the types of C++ Operators" << endl;

    cout << ">>>> Logical Operators" << endl;
    cout << ">>>>>>>> The value of Logical's AND operator i.e. ((" << num_1 << " == " << num_2 << ")"
         << " && (" << num_1 << " <= " << num_2 << "))"
         << " is " << ((num_1 == num_2) && (num_1 <= num_2)) << endl;
    cout << ">>>>>>>> The value of Logical's OR operator i.e. ((" << num_1 << " == " << num_2 << ")"
         << " || (" << num_1 << " <= " << num_2 << "))"
         << " is " << ((num_1 == num_2) || (num_1 <= num_2)) << endl;
    cout << ">>>>>>>> The value of Logical's NOT operator i.e. (!(" << num_1 << " == " << num_2 << ")) is " << (!(num_1 == num_2)) << endl;

    return 0;
}

```

---

---

## **_12.) tutorial_6_2_5 of C/C++_**

### [**_Click me_**](tutorial_6_2_5.cpp "Clike here to see full file") to see full file of tutorial_6_2_5

```C++
// Date 25-05-2021

#include <iostream>
using namespace std;

int main()
{
    int num_1, num_2;

    cout << "Please Enter the value of num_1" << endl;
    cin >> num_1;
    cout << "Please Enter the value of num_2" << endl;
    cin >> num_2;
    cout << endl;

    cout << "Operators in C++" << endl;
    cout << "Following are the types of C++ Operators" << endl;

    cout << ">>>> Bitwise Operators" << endl;
    cout << ">>>>>>>> The value of Bitwise's AND \'&\' operator i.e. (" << num_1 << " & " << num_2 << ") is " << (num_1 & num_2) << endl;
    cout << ">>>>>>>> The value of Bitwise's OR \'|\' operator i.e. (" << num_1 << " | " << num_2 << ") is " << (num_1 | num_2) << endl;
    cout << ">>>>>>>> The value of Bitwise's NOT \'~\' operator i.e. (~" << num_1 << ") is " << (~num_1) << " and (~" << num_2 << ") is " << (~num_2) << endl;
    cout << ">>>>>>>> The value of Bitwise's XOR \'^\' operator i.e. (" << num_1 << " ^ " << num_2 << ") is " << (num_1 ^ num_2) << endl;
    cout << ">>>>>>>> The value of Bitwise's Left Shift \'<<\' operator i.e. (" << num_1 << " << " << num_2 << ") is " << (num_1 << num_2) << endl;
    cout << ">>>>>>>> The value of Bitwise's Right Shift \'>>\' operator i.e. (" << num_1 << " >> " << num_2 << ") is " << (num_1 >> num_2) << endl;
    return 0;
}

```

---

---

## **_13.) tutorial_7_0 of C/C++_**

### [**_Click me_**](tutorial_7_0.cpp "Clike here to see full file") to see full file of tutorial_7_0

```C++
// Date 26-05-2021
#include <iostream>

using namespace std;

int variable_7_1 = 2;

int main()
{
    int variable_7_1 = 45;
    cout << ">>>> Using a global variable in a function" << endl;
    cout << ">>>>>>>> Variable of name \'variable_7_1\' which is defined inside a function is " << variable_7_1 << endl;
    cout << ">>>>>>>> Variable of name \'variable_7_1\' which is defined in Global Scope i.e. outside a function; and using it by adding \'::\' before variable name is " << ::variable_7_1 << endl;

    int variable_7_2_int = 2;
    float variable_7_2_float = 8.4;
    char variable_7_2_char = 's';
    double variable_7_2_double = 45;
    cout << ">>>> Literals" << endl;
    cout << ">>>>>>>> Size of an \'int\' Data Type is " << sizeof(variable_7_2_int) << endl;
    cout << ">>>>>>>> Size of an \'float\' Data Type is " << sizeof(variable_7_2_float) << endl;
    cout << ">>>>>>>> Size of an \'char\' Data Type is " << sizeof(variable_7_2_char) << endl;
    cout << ">>>>>>>> Size of an \'double\' Data Type is " << sizeof(variable_7_2_double) << endl;
    cout << ">>>>>>>> Size of \'148.48\' is " << sizeof(148.48) << endl;
    cout << ">>>>>>>> Size of \'148.48f\' is " << sizeof(148.48f) << endl;
    cout << ">>>>>>>> Size of \'148.48F\' is " << sizeof(148.48F) << endl;
    cout << ">>>>>>>> Size of \'148.48l\' is " << sizeof(148.48l) << endl;
    cout << ">>>>>>>> Size of \'148.48L\' is " << sizeof(148.48L) << endl;

    int variable_7_3_var1 = 2;
    int &variable_7_3_var2 = variable_7_3_var1;
    int &variable_7_3_var3 = variable_7_3_var2;
    cout << ">>>> Reference Variables" << endl;
    cout << ">>>>>>>> Value of variable name \'variable_7_3_var1\' is " << variable_7_3_var1 << endl;
    cout << ">>>>>>>> Value of variable name \'variable_7_3_var2\' is " << variable_7_3_var2 << endl;
    cout << ">>>>>>>> Value of variable name \'variable_7_3_var3\' is " << variable_7_3_var3 << endl;
    cout << ">>>>>>>> Rember no copy is been made of any variable both variable are same if any change is applied to any of the variable that change will also aplicable on another variable." << endl;

    float variable_7_4_float = 12.4548;
    cout << ">>>> Type Casting" << endl;
    cout << ">>>>>>>> Value of variable name \'variable_7_4_float\' is " << variable_7_4_float << endl;
    cout << ">>>>>>>> Value of variable name \'variable_7_4_float\' after Type Casting into int is " << int(variable_7_4_float) << endl;
    cout << ">>>>>>>> You can simpley do Type Casting by writing the following syntax:" << endl;
    cout << ">>>>>>>> type_in_which_you_need_to_TypeCast_your_variable(variable)" << endl;
    cout << ">>>>>>>> Or" << endl;
    cout << ">>>>>>>> (type_in_which_you_need_to_TypeCast_your_variable)variable" << endl;
    return 0;
}

```

---

---

## **_14.) tutorial_7_1 of C/C++_**

### [**_Click me_**](tutorial_7_1.cpp "Clike here to see full file") to see full file of tutorial_7_1

```C++
// Date 26-05-2021
#include <iostream>

using namespace std;

int variable_7_1 = 2;

int main()
{
    int variable_7_1 = 45;
    cout << ">>>> Using a global variable in a function" << endl;
    cout << ">>>>>>>> Variable of name \'variable_7_1\' which is defined inside a function is " << variable_7_1 << endl;
    cout << ">>>>>>>> Variable of name \'variable_7_1\' which is defined in Global Scope i.e. outside a function; and using it by adding \'::\' before variable name is " << ::variable_7_1 << endl;
    return 0;
}

```

---

---

## **_15.) tutorial_7_2 of C/C++_**

### [**_Click me_**](tutorial_7_2.cpp "Clike here to see full file") to see full file of tutorial_7_2

```C++
// Date 26-05-2021
#include <iostream>

using namespace std;

int main()
{
    int variable_7_2_int = 2;
    float variable_7_2_float = 8.4;
    char variable_7_2_char = 's';
    double variable_7_2_double = 45;

    cout << ">>>> Literals" << endl;
    cout << ">>>>>>>> Size of an \'int\' Data Type is " << sizeof(variable_7_2_int) << endl;
    cout << ">>>>>>>> Size of an \'float\' Data Type is " << sizeof(variable_7_2_float) << endl;
    cout << ">>>>>>>> Size of an \'char\' Data Type is " << sizeof(variable_7_2_char) << endl;
    cout << ">>>>>>>> Size of an \'double\' Data Type is " << sizeof(variable_7_2_double) << endl;
    cout << ">>>>>>>>" << endl;
    cout << ">>>>>>>> Size of \'148.48\' is " << sizeof(148.48) << endl;
    cout << ">>>>>>>> Size of \'148.48f\' is " << sizeof(148.48f) << endl;
    cout << ">>>>>>>> Size of \'148.48F\' is " << sizeof(148.48F) << endl;
    cout << ">>>>>>>> Size of \'148.48l\' is " << sizeof(148.48l) << endl;
    cout << ">>>>>>>> Size of \'148.48L\' is " << sizeof(148.48L) << endl;
    return 0;
}

```

---

---

## **_16.) tutorial_7_3 of C/C++_**

### [**_Click me_**](tutorial_7_3.cpp "Clike here to see full file") to see full file of tutorial_7_3

```C++
// Date 26-05-2021
#include <iostream>

using namespace std;

int main()
{
    int variable_7_3_var1 = 2;
    int &variable_7_3_var2 = variable_7_3_var1;
    int &variable_7_3_var3 = variable_7_3_var2;

    cout << ">>>> Reference Variables" << endl;
    cout << ">>>>>>>> Value of variable name \'variable_7_3_var1\' is " << variable_7_3_var1 << endl;
    cout << ">>>>>>>> Value of variable name \'variable_7_3_var2\' is " << variable_7_3_var2 << endl;
    cout << ">>>>>>>> Value of variable name \'variable_7_3_var3\' is " << variable_7_3_var3 << endl;
    cout << ">>>>>>>> Rember no copy is been made of any variable both variable are same if any change is applied to any of the variable that change will also aplicable on another variable." << endl;
    return 0;
}

```

---

---

## **_17.) tutorial_7_4 of C/C++_**

### [**_Click me_**](tutorial_7_4.cpp "Clike here to see full file") to see full file of tutorial_7_4

```C++
// Date 26-05-2021
#include <iostream>

using namespace std;

int main()
{
    float variable_7_4_float = 12.4548;

    cout << ">>>> Type Casting" << endl;
    cout << ">>>>>>>> Value of variable name \'variable_7_4_float\' is " << variable_7_4_float << endl;
    cout << ">>>>>>>> Value of variable name \'variable_7_4_float\' after Type Casting into int is " << int(variable_7_4_float) << endl;
    cout << ">>>>>>>> You can simpley do Type Casting by writing the following syntax:" << endl;
    cout << ">>>>>>>> type_in_which_you_need_to_TypeCast_your_variable(variable)" << endl;
    cout << ">>>>>>>> Or" << endl;
    cout << ">>>>>>>> (type_in_which_you_need_to_TypeCast_your_variable)variable" << endl;
    return 0;
}

```

---

---

## **_18.) tutorial_8_0 of C/C++_**

### [**_Click me_**](tutorial_8_0.cpp "Clike here to see full file") to see full file of tutorial_8_0

```C++
// Date 27-05-2021

#include <iostream>
#include <iomanip>

using namespace std;

int main(int argc, char const *argv[])
{
    const int variable_8_1 = 77;
    //*the below line of code will give an error
    // variable_8_1 = 2;
    //*the above line of code will give an error
    cout << ">>>> Constants in C++" << endl;
    cout << ">>>>>>>> To create a constants variable in C++ just write constant before the syntax of declaring a Variable for example: " << endl;
    cout << ">>>>>>>> const int variable_8_1 = 77;" << endl;

    int variable_8_2_1 = 21, variable_8_2_2 = 7814, variable_8_2_3 = 874652;
    cout << ">>>> Manipulators in C++" << endl;
    cout << ">>>>>>>> Value of variable name variable_8_2_1 is:" << setw(9) << variable_8_2_1 << endl;
    cout << ">>>>>>>> Value of variable name variable_8_2_2 is:" << setw(9) << variable_8_2_2 << endl;
    cout << ">>>>>>>> Value of variable name variable_8_2_3 is:" << setw(9) << variable_8_2_3 << endl;

    cout << ">>>> Operator Precendence" << endl;
    cout
        << ">>>>>>>> The value of 2 + 3 * 6 / 6 * 7 - 9 is: " << 2 + 3 * 6 / 6 * 7 - 9 << endl;
    return 0;
}

```

---

---

## **_19.) tutorial_8_1 of C/C++_**

### [**_Click me_**](tutorial_8_1.cpp "Clike here to see full file") to see full file of tutorial_8_1

```C++
// Date 27-05-2021

#include <iostream>

using namespace std;

int main()
{
    const int variable_8_1 = 77;

    //*the below line of code will give an error
    // variable_8_1 = 2;
    //*the above line of code will give an error
    cout << ">>>> Constants in C++" << endl;
    cout << ">>>>>>>> To create a constants variable in C++ just write constant before the syntax of declaring a Variable for example: " << endl;
    cout << ">>>>>>>> const int variable_8_1 = 77;" << endl;
    return 0;
}

```

---

---

## **_20.) tutorial_8_2 of C/C++_**

### [**_Click me_**](tutorial_8_2.cpp "Clike here to see full file") to see full file of tutorial_8_2

```C++
// Date 27-05-2021

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int variable_8_2_1 = 21, variable_8_2_2 = 7814, variable_8_2_3 = 874652;
    cout << ">>>> Manipulators in C++" << endl;
    cout << ">>>>>>>> Value of variable name variable_8_2_1 is:" << setw(9) << variable_8_2_1 << endl;
    cout << ">>>>>>>> Value of variable name variable_8_2_2 is:" << setw(9) << variable_8_2_2 << endl;
    cout << ">>>>>>>> Value of variable name variable_8_2_3 is:" << setw(9) << variable_8_2_3 << endl;
    return 0;
}

```

---

---

## **_21.) tutorial_8_3 of C/C++_**

### [**_Click me_**](tutorial_8_3.cpp "Clike here to see full file") to see full file of tutorial_8_3

```C++
// Date 27-05-2021

#include <iostream>

using namespace std;

int main()
{
    cout << ">>>> Operator Precendence" << endl;
    cout << ">>>>>>>> The value of 2 + 3 * 6 / 6 * 7 - 9 is: " << 2 + 3 * 6 / 6 * 7 - 9 << endl;
    return 0;
}

```

---

---

## **_22.) tutorial_9_1 of C/C++_**

### [**_Click me_**](tutorial_9_1.cpp "Clike here to see full file") to see full file of tutorial_9_1

```C++
// Date 28-05-2021

#include <iostream>

using namespace std;

int main()
{
    int age;
    cout << "What is Your Age!" << endl;
    cin >> age;
    if (age < 0)
    {
        cout << "Your age is " << age << " which is not a valid age please enter a valid age and try again!" << endl;
    }
    else if (age < 18)
    {
        cout << "Your age is " << age << " which is a small age to drink Beer, So you can't drink Beer!" << endl;
    }
    else if (age == 18)
    {
        cout << "Your age is 18 so you can drink Beer next Year!" << endl;
    }
    else if (age > 18 && age < 60)
    {
        cout << "Your age is " << age << " so you can drink Beer!" << endl;
    }
    else if (age >= 60)
    {
        cout << "Your age is " << age << " which is to much and it can be dangerous in this age to drink so you can't drink Beer!" << endl;
    }

    return 0;
}

```

---

---

## **_23.) tutorial_9_2 of C/C++_**

### [**_Click me_**](tutorial_9_2.cpp "Clike here to see full file") to see full file of tutorial_9_2

```C++
// Date 28-05-2021

#include <iostream>

using namespace std;

int main()
{
    int age;
    cout << "What is Your Age!" << endl;
    cin >> age;
    switch (age)
    {
    case 0:
        cout << "Your age is 0 so you can't drink Beer!" << endl;
        break;
    case 18:
        cout << "Your age is 18 so you can drink Beer next Year!" << endl;
        break;
    case 19:
        cout << "Your age is 19 so you can drink Beer!" << endl;
        break;
    case 45:
        cout << "Your age is 45 so you can drink Beer!" << endl;
        break;
    case 60:
        cout << "Your age is 60 so you can drink Beer but don't drink much!" << endl;
        break;
    default:
        break;
    }
    return 0;
}

```

---

---

## **_24.) tutorial_10_1_1 of C/C++_**

### [**_Click me_**](tutorial_10_1_1.cpp "Clike here to see full file") to see full file of tutorial_10_1_1

```C++
// Date 28-05-2021

#include <iostream>

using namespace std;

int main()
{
    for (int i = 1; i <= 100; i++)
    {
        cout << i << endl;
    }

    return 0;
}

```

---

---

## **_25.) tutorial_10_1_2 of C/C++_**

### [**_Click me_**](tutorial_10_1_2.cpp "Clike here to see full file") to see full file of tutorial_10_1_2

```C++
// Date 28-05-2021

#include <iostream>

using namespace std;

int main()
{
    int i = 1;
    while (i <= 100)
    {
        cout << i++ << endl;
    }

    return 0;
}

```

---

---

## **_26.) tutorial_10_1_3_1 of C/C++_**

### [**_Click me_**](tutorial_10_1_3_1.cpp "Clike here to see full file") to see full file of tutorial_10_1_3_1

```C++
// Date 28-05-2021

#include <iostream>

using namespace std;

int main()
{
    int i = 1;
    do
    {
        cout << i++ << endl;
    } while (i <= 100);

    return 0;
}

```

---

---

## **_27.) tutorial_10_1_3_1_2 of C/C++_**

### [**_Click me_**](tutorial_10_1_3_1_2.cpp "Clike here to see full file") to see full file of tutorial_10_1_3_1_2

```C++
// Date 28-05-2021

#include <iostream>

using namespace std;

int main()
{
    int i = 1;
    //* Note: do while loop will execute atleast once
    do
    {
        cout << i++ << endl;
    } while (false);
    //* Note: do while loop will execute atleast once
    return 0;
}

```

---

---

## **_28.) tutorial_10_2_quiz of C/C++_**

### [**_Click me_**](tutorial_10_2_quiz.cpp "Clike here to see full file") to see full file of tutorial_10_2_quiz

```C++
// Date 28-05-2021
//* Make a Multiplacation Table of 6 using do while loop
//* Make a Multiplacation Table of 6 using do while loop
//* Make a Multiplacation Table of 6 using do while loop
//* Make a Multiplacation Table of 6 using do while loop
//* Make a Multiplacation Table of 6 using do while loop
//* Make a Multiplacation Table of 6 using do while loop
//* Make a Multiplacation Table of 6 using do while loop
//* Make a Multiplacation Table of 6 using do while loop
//* Make a Multiplacation Table of 6 using do while loop
//* Make a Multiplacation Table of 6 using do while loop
#include <iostream>

using namespace std;

int main()
{
    int i = 6;
    int number_of_time_table_printed = 1;
    do
    {
        cout << "6 * " << number_of_time_table_printed++ << " = " << i << endl;
        i = i + 6;
    } while (i <= 60);
    return 0;
}

```

---

---

## **_29.) tutorial_11_1 of C/C++_**

### [**_Click me_**](tutorial_11_1.cpp "Clike here to see full file") to see full file of tutorial_11_1

```C++
// Date 29-05-2021

#include <iostream>

using namespace std;

int main()
{
    for (int i = 0; i <= 100; i++)
    {
        if (i == 10)
        {
            break;
        }
        cout << "Hello Aman " << i << " time!" << endl;
    }
    return 0;
}
```

---

---

## **_30.) tutorial_11_2 of C/C++_**

### [**_Click me_**](tutorial_11_2.cpp "Clike here to see full file") to see full file of tutorial_11_2

```C++
// Date 29-05-2021

#include <iostream>

using namespace std;

int main()
{
    for (int i = 0; i <= 100; i++)
    {
        if (i == 10)
        {
            continue;
        }
        cout << "Hello Aman " << i << " time!" << endl;
    }
    return 0;
}
```

---

---

## **_31.) tutorial_12 of C/C++_**

### [**_Click me_**](tutorial_12.cpp "Clike here to see full file") to see full file of tutorial_12

```C++
// Date 29-05-2021

#include <iostream>

using namespace std;

int main()
{
    int variable_12_1 = 10;
    int *address_1 = &variable_12_1;
    cout << &variable_12_1 << endl
         << *address_1 << endl;

    // int variable_12_2 = 10;
    // int *address_2 = &variable_12_2;
    // cout << &address_2 << endl;

    // cout << &variable_12_1 << endl;

    return 0;
}
```

---

---

## **_32.) tutorial_13_1_1_1 of C/C++_**

### [**_Click me_**](tutorial_13_1_1_1.cpp "Clike here to see full file") to see full file of tutorial_13_1_1_1

```C++
// Date 29-05-2021

#include <iostream>

using namespace std;

int main()
{
    int array_1[10] = {12, 3, 45, 7, 6, 12, 87, 34, 45, 23};
    for (int i = 0; i < 10; i++)
    {
        cout << "Value of array_1[" << i << "] is " << array_1[i] << endl;
    }
    return 0;
}

```

---

---

## **_33.) tutorial_13_1_1_2 of C/C++_**

### [**_Click me_**](tutorial_13_1_1_2.cpp "Clike here to see full file") to see full file of tutorial_13_1_1_2

```C++
// Date 29-05-2021

#include <iostream>

using namespace std;

int main()
{
    char name[4] = {'A',
                    'm',
                    'a',
                    'n'};
    cout << "Hello ";
    for (int i = 0; i < 4; i++)
    {

        cout << name[i];
    }

    return 0;
}
```

---

---

## **_34.) tutorial_13_1_2 of C/C++_**

### [**_Click me_**](tutorial_13_1_2.cpp "Clike here to see full file") to see full file of tutorial_13_1_2

```C++
// Date 29-05-2021

#include <iostream>

using namespace std;

int main()
{
    int array_1[10] = {12, 3, 45, 7, 6, 12, 87, 34, 45, 23};
    int *pointer = array_1;
    for (int i = 0; i < 10; i++)
    {
        cout << "Value of array_1[" << i << "] location is " << pointer << " and it's value is " << *pointer++ << endl;
    }

    return 0;
}
```

---

---

## **_35.) tutorial_13_2_1_quiz of C/C++_**

### [**_Click me_**](tutorial_13_2_1_quiz.cpp "Clike here to see full file") to see full file of tutorial_13_2_1_quiz

```C++
// Date 29-05-2021

//* Make an array of 10 indices and print it using while loop
//* Make an array of 10 indices and print it using while loop
//* Make an array of 10 indices and print it using while loop
//* Make an array of 10 indices and print it using while loop
//* Make an array of 10 indices and print it using while loop
//* Make an array of 10 indices and print it using while loop
//* Make an array of 10 indices and print it using while loop
//* Make an array of 10 indices and print it using while loop
//* Make an array of 10 indices and print it using while loop
//* Make an array of 10 indices and print it using while loop

#include <iostream>

using namespace std;

int main()
{
    int array_1[10] = {12, 3, 45, 7, 6, 12, 87, 34, 45, 23};
    int i = 0;
    while (i < 10)
    {

        cout << "Value of array_1[" << i << "] is " << array_1[i++] << endl;
    }
    return 0;
}

```

---

---

## **_36.) tutorial_13_2_2_quiz of C/C++_**

### [**_Click me_**](tutorial_13_2_2_quiz.cpp "Clike here to see full file") to see full file of tutorial_13_2_2_quiz

```C++
// Date 29-05-2021

//* Make an array of 10 indices and print it using do while loop
//* Make an array of 10 indices and print it using do while loop
//* Make an array of 10 indices and print it using do while loop
//* Make an array of 10 indices and print it using do while loop
//* Make an array of 10 indices and print it using do while loop
//* Make an array of 10 indices and print it using do while loop
//* Make an array of 10 indices and print it using do while loop
//* Make an array of 10 indices and print it using do while loop
//* Make an array of 10 indices and print it using do while loop
//* Make an array of 10 indices and print it using do while loop

#include <iostream>

using namespace std;

int main()
{
    int array_1[10] = {12, 3, 45, 7, 6, 12, 87, 34, 45, 23};
    int i = 0;
    do
    {

        cout << "Value of array_1[" << i << "] is " << array_1[i++] << endl;
    } while (i < 10);
    return 0;
}

```

---

---

## **_37.) tutorial_14_1_1 of C/C++_**

### [**_Click me_**](tutorial_14_1_1.cpp "Clike here to see full file") to see full file of tutorial_14_1_1

```C++
// Date 29-05-2021

#include <iostream>

using namespace std;

struct employee
{
    int employee_id;
    char employee_favorite_character;
    float employee_salary;
};

int main()
{
    struct employee suresh;
    suresh.employee_id = 78179;
    suresh.employee_favorite_character = 'A';
    suresh.employee_salary = 7845.14;

    struct employee rohan;
    rohan.employee_id = 17844;
    rohan.employee_favorite_character = 'R';
    rohan.employee_salary = 14551.65;

    cout << "Suresh's Id is " << suresh.employee_id << endl;
    cout << "Suresh's Favorite Character is " << suresh.employee_favorite_character << endl;
    cout << "Suresh's Salary is " << suresh.employee_salary << endl;

    cout << "Rohan's Id is " << rohan.employee_id << endl;
    cout << "Rohan's Favorite Character is " << rohan.employee_favorite_character << endl;
    cout << "Rohan's Salary is " << rohan.employee_salary << endl;

    return 0;
}
```

---

---

## **_38.) tutorial_14_1_2 of C/C++_**

### [**_Click me_**](tutorial_14_1_2.cpp "Clike here to see full file") to see full file of tutorial_14_1_2

```C++
// Date 29-05-2021

#include <iostream>
#include <iomanip>

using namespace std;

typedef struct employee
{
    int employee_id;
    char employee_favorite_character;
    float employee_salary;
} em;

int main()
{
    em suresh;
    suresh.employee_id = 78179;
    suresh.employee_favorite_character = 'A';
    suresh.employee_salary = 7845.14;

    em rohan;
    rohan.employee_id = 17844;
    rohan.employee_favorite_character = 'R';
    rohan.employee_salary = 14551.65;

    cout << "Suresh's Id is " << suresh.employee_id << endl;
    cout << "Suresh's Favorite Character is " << suresh.employee_favorite_character << endl;
    cout << "Suresh's Salary is " << suresh.employee_salary << endl;

    cout << "Rohan's Id is " << rohan.employee_id << endl;
    cout << "Rohan's Favorite Character is " << rohan.employee_favorite_character << endl;
    cout << "Rohan's Salary is " << rohan.employee_salary << endl;

    return 0;
}
```

---

---

## **_39.) tutorial_14_2 of C/C++_**

### [**_Click me_**](tutorial_14_2.cpp "Clike here to see full file") to see full file of tutorial_14_2

```C++
// Date 29-05-2021

#include <iostream>

using namespace std;

union money
{
    int food;
    float wheat_in_kg;
    char material;
};

int main()
{
    union money u1;
    u1.food = 7812;
    cout << "Value of food before changing is: " << u1.food << endl;
    u1.material = 'V';
    cout << "Value of food after changing is: " << u1.food << endl;
    cout << "Value of material after value of food changing is: " << u1.material << endl;

    return 0;
}
```

---

---

## **_40.) tutorial_14_3 of C/C++_**

### [**_Click me_**](tutorial_14_3.cpp "Clike here to see full file") to see full file of tutorial_14_3

```C++
// Date 29-05-2021

#include <iostream>

using namespace std;

int main()
{
    enum meal
    {
        breakfast,
        lunch,
        dinner
    };
    cout << "Value of meal " << breakfast << " is: " << breakfast << endl;
    cout << "Value of meal " << lunch << " is: " << lunch << endl;
    cout << "Value of meal " << dinner << " is: " << dinner << endl;

    meal var_1 = dinner;
    cout << "Value of var_1 is: " << var_1 << endl;
    return 0;
}
```

---

---

## **_41.) tutorial_15 of C/C++_**

### [**_Click me_**](tutorial_15.cpp "Clike here to see full file") to see full file of tutorial_15

```C++
// Date 30-05-2021

#include <iostream>

using namespace std;

void for_printing(void)
{
    cout << "Hello!" << endl;
}
int square(int);
int main()
{
    int num1;
    cout << "Please enter a number to know it's sqare" << endl;
    cin >> num1;
    cout << square(num1) << endl;
    for_printing();

    return 0;
}

int square(int x)
{
    int y;
    y = x * x;
    return y;
}

```

---

---

## **_42.) tutorial_16_0 of C/C++_**

### [**_Click me_**](tutorial_16_0.cpp "Clike here to see full file") to see full file of tutorial_16_0

```C++
// Date 30-05-2021

#include <iostream>

using namespace std;

int swap(int a, int b)
{
    //* Note: This funtion will absolutely not the variable values because this function just maked a copy of the given variable to it
    //* To do swaping you need to make use of their locations i.e. their pointers
    //* Note: This method of accessing variables is known as Call by value
    //* Note: This method of accessing variables is known as Call by value
    //* Note: This method of accessing variables is known as Call by value
    //* Note: This method of accessing variables is known as Call by value
    //* Note: This method of accessing variables is known as Call by value
    int temporary_variable = a;
    a = b;
    b = temporary_variable;
    return 0;
}

int swap_using_pointers(int *a, int *b)
{
    //* Note: This method of accessing variables is known as Call by refrence
    int temporary_variable = *a;
    *a = *b;
    *b = temporary_variable;
    return 0;
}

int swap_using_reference(int &a, int &b)
{
    int temporary_variable = a;
    a = b;
    b = temporary_variable;
    return 0;
}

int main()
{
    int x = 32, y = 12;

    cout << endl
         << "1.) Values of x and y are respectively (without swap)" << endl
         << "x = " << x << endl
         << "y = " << y << endl
         << endl;
    swap(y, x);
    cout
        << "2.) Now values of x and y are respectively (with variable swaping)" << endl
        << "x = " << x << endl
        << "y = " << y << endl
        << endl;
    swap_using_pointers(&x, &y);
    cout << "3.) Now values of x and y are respectively (with pointer swaping)" << endl
         << "x = " << x << endl
         << "y = " << y << endl
         << endl;
    x = 32;
    y = 12;
    cout << "4.) Values of x and y are reseted and their values are (without swap)" << endl
         << "x = " << x << endl
         << "y = " << y << endl
         << endl;
    swap_using_reference(x, y);
    cout << "5.) Now values of x and y are respectively (with reference swaping)" << endl
         << "x = " << x << endl
         << "y = " << y << endl
         << endl;

    return 0;
}
```

---

---

## **_43.) tutorial_16_1 of C/C++_**

### [**_Click me_**](tutorial_16_1.cpp "Clike here to see full file") to see full file of tutorial_16_1

```C++
// Date 30-05-2021

#include <iostream>

using namespace std;

int swap(int a, int b)
{
    //* Note: This funtion will absolutely not the variable values because this function just maked a copy of the given variable to it
    //* To do swaping you need to make use of their locations i.e. their pointers
    //* Note: This method of accessing variables is known as Call by value
    //* Note: This method of accessing variables is known as Call by value
    //* Note: This method of accessing variables is known as Call by value
    //* Note: This method of accessing variables is known as Call by value
    //* Note: This method of accessing variables is known as Call by value
    int temporary_variable = a;
    a = b;
    b = temporary_variable;
    return 0;
}

int main()
{
    int x = 32, y = 12;

    cout << endl
         << "Values of x and y are respectively (without swap)" << endl
         << "x = " << x << endl
         << "y = " << y << endl
         << endl;
    swap(y, x);
    cout
        << "Now values of x and y are respectively (with variable swaping)" << endl
        << "x = " << x << endl
        << "y = " << y << endl
        << endl;
    return 0;
}
```

---

---

## **_44.) tutorial_16_2 of C/C++_**

### [**_Click me_**](tutorial_16_2.cpp "Clike here to see full file") to see full file of tutorial_16_2

```C++
// Date 30-05-2021

#include <iostream>

using namespace std;

int swap_using_pointers(int *a, int *b)
{
    //* Note: This method of accessing variables is known as Call by refrence
    int temporary_variable = *a;
    *a = *b;
    *b = temporary_variable;
    return 0;
}

int main()
{
    int x = 32, y = 12;

    cout << endl
         << "Values of x and y are respectively (without swap)" << endl
         << "x = " << x << endl
         << "y = " << y << endl
         << endl;
    swap_using_pointers(&x, &y);
    cout << "Now values of x and y are respectively (with pointer swaping)" << endl
         << "x = " << x << endl
         << "y = " << y << endl
         << endl;
    return 0;
}
```

---

---

## **_45.) tutorial_16_3 of C/C++_**

### [**_Click me_**](tutorial_16_3.cpp "Clike here to see full file") to see full file of tutorial_16_3

```C++
// Date 30-05-2021

#include <iostream>

using namespace std;

int swap_using_reference(int &a, int &b)
{
    int temporary_variable = a;
    a = b;
    b = temporary_variable;
    return 0;
}

int main()
{
    int x = 32, y = 12;

    cout << endl
         << "Values of x and y are respectively (without swap)" << endl
         << "x = " << x << endl
         << "y = " << y << endl
         << endl;
    swap_using_reference(x, y);
    cout << "Now values of x and y are respectively (with reference swaping)" << endl
         << "x = " << x << endl
         << "y = " << y << endl
         << endl;

    return 0;
}
```

---

---

## **_46.) tutorial_17_0 of C/C++_**

### [**_Click me_**](tutorial_17_0.cpp "Clike here to see full file") to see full file of tutorial_17_0

```C++
// Date 30-05-2021

#include <iostream>

using namespace std;

inline int func_1(int a, int b) { return a * b; }

int main()
{
    int a, b;
    cout << "Please enter the value for A!" << endl;
    cin >> a;
    cout << "Please enter the value for B!" << endl;
    cin >> b;

    cout << "Function return's value is!" << endl
         << func_1(a, b);

    return 0;
}
```

---

---

## **_47.) tutorial_17_1 of C/C++_**

### [**_Click me_**](tutorial_17_1.cpp "Clike here to see full file") to see full file of tutorial_17_1

```C++
// Date 30-05-2021

#include <iostream>

using namespace std;

int calculation(int a, int b)
{
    static int c = 2;
    //* Note: After function execution stops the only value which not gets destroyed is the value of a static variable
    return a * b + c++;
    //* Note: After function execution stops the only value which not gets destroyed is the value of a static variable
}

int main()
{
    int a, b;
    cout << "Please enter the value for A!" << endl;
    cin >> a;
    cout << "Please enter the value for B!" << endl;
    cin >> b;

    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;
    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;
    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;
    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;
    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;
    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;
    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;
    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;
    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;
    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;
    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;
    cout << "Function return's value is!" << endl
         << calculation(a, b) << endl;

    return 0;
}
```

---

---

## **_48.) tutorial_17_2 of C/C++_**

### [**_Click me_**](tutorial_17_2.cpp "Clike here to see full file") to see full file of tutorial_17_2

```C++
// Date 30-05-2021

#include <iostream>

using namespace std;

float intrest_money_calculator(int money, float intrest_precent = 1.04)
{
    return money * intrest_precent;
}

int main()
{
    int money;
    cout << "Please enter the value of Money!" << endl;
    cin >> money;

    cout << "Your's money + intrest added value is!" << endl
         << intrest_money_calculator(money) << endl;

    cout << "If you are POOR then money + intrest added value is!" << endl
         << intrest_money_calculator(money, 1.1) << endl;

    return 0;
}
```

---

---

## **_49.) tutorial_18_1 of C/C++_**

### [**_Click me_**](tutorial_18_1.cpp "Clike here to see full file") to see full file of tutorial_18_1

```C++
// Date 31-05-2021

#include <iostream>

using namespace std;

int factorial_calculator(int n)
{
    int output = 1;
    if (n == 0)
    {
        return output;
    }
    while (n >= 2)
    {
        output = output * n--;
    }
    return output;
}

int main()
{
    int n;
    cout << "Please enter a number to know it's factorial of!" << endl;
    cin >> n;
    cout << "The value of factorial of " << n << " is: " << factorial_calculator(n) << endl;
    return 0;
}
```

---

---

## **_50.) tutorial_18_2 of C/C++_**

### [**_Click me_**](tutorial_18_2.cpp "Clike here to see full file") to see full file of tutorial_18_2

```C++
// Date 31-05-2021

// * In previous code(i.e. "tutorial_18_1.cpp") of finding we had written a long function to find the factorial of but in this code we will write a function which uses reccrussion to find the factorial off
// * In previous code(i.e. "tutorial_18_1.cpp") of finding we had written a long function to find the factorial of but in this code we will write a function which uses reccrussion to find the factorial off
// * In previous code(i.e. "tutorial_18_1.cpp") of finding we had written a long function to find the factorial of but in this code we will write a function which uses reccrussion to find the factorial off
// * In previous code(i.e. "tutorial_18_1.cpp") of finding we had written a long function to find the factorial of but in this code we will write a function which uses reccrussion to find the factorial off
// * In previous code(i.e. "tutorial_18_1.cpp") of finding we had written a long function to find the factorial of but in this code we will write a function which uses reccrussion to find the factorial off
// * In previous code(i.e. "tutorial_18_1.cpp") of finding we had written a long function to find the factorial of but in this code we will write a function which uses reccrussion to find the factorial off
// * In previous code(i.e. "tutorial_18_1.cpp") of finding we had written a long function to find the factorial of but in this code we will write a function which uses reccrussion to find the factorial off
// * In previous code(i.e. "tutorial_18_1.cpp") of finding we had written a long function to find the factorial of but in this code we will write a function which uses reccrussion to find the factorial off
// * In previous code(i.e. "tutorial_18_1.cpp") of finding we had written a long function to find the factorial of but in this code we will write a function which uses reccrussion to find the factorial off
// * In previous code(i.e. "tutorial_18_1.cpp") of finding we had written a long function to find the factorial of but in this code we will write a function which uses reccrussion to find the factorial off

#include <iostream>

using namespace std;

int factorial_calculator(int n)
{
    if (n <= 1)
    {
        return 1;
    }
    return n * factorial_calculator(n - 1);
}

int fibonacci_calculator(int n)
{
    if (n < 2)
    {
        return 1;
    }
    return fibonacci_calculator(n - 1) + fibonacci_calculator(n - 2);
}

int main()
{
    int n;
    cout << "Please enter a number to know it's factorial and fibonacci of!" << endl;
    cin >> n;
    cout << "The value of factorial of " << n << " is: " << factorial_calculator(n) << endl
         << "The value of fibonacci of " << n << " is: " << fibonacci_calculator(n) << endl;
    return 0;
}
```

---

---

## **_51.) tutorial_19_1 of C/C++_**

### [**_Click me_**](tutorial_19_1.cpp "Clike here to see full file") to see full file of tutorial_19_1

```C++
// Date 31-05-2021

#include <iostream>

using namespace std;

int sum(int a, int b, int c)
{
    cout << "Using function with three argunments" << endl;
    return a + b + c;
}
int sum(int a, int b)
{
    cout << "Using function with two argunments" << endl;
    return a + b;
}

int main()
{
    cout << "The value of 3 + 7 (using sum function) is: " << sum(3, 7) << endl;
    cout << "The value of 3 + 7 + 10 (using sum function) is: " << sum(3, 7, 10) << endl;
    return 0;
}
```

---

---

## **_52.) tutorial_19_2 of C/C++_**

### [**_Click me_**](tutorial_19_2.cpp "Clike here to see full file") to see full file of tutorial_19_2

```C++
// Date 31-05-2021

#include <iostream>

using namespace std;

int volume(int side)
{
    //* Volume of cube
    return side * side * side;
}
int volume(int length, int breadth, int height)
{
    //* Volume of cuboid
    return length * breadth * height;
}
double volume(double radius, double height)
{
    //* Volume of cylinder
    return 3.14285714286 * radius * radius * height;
}
int main()
{
    cout << "The Volume of Cube with side 3 is: " << endl
         << volume(3) << " >>>>>>>>>> Using function named volume(i.e. same name but diffrent arguments function)" << endl;
    cout << "The Volume of Cuboid with side 3, 7 and 10  is: " << endl
         << volume(3, 7, 10) << " >>>>>>>>>> Using function named volume(i.e. same name but diffrent arguments function)" << endl;
    cout << "The Volume of Cylinder with height 23 and radius 6 is: " << endl
         << volume(6, 23) << " >>>>>>>>>> Using function named volume(i.e. same name but diffrent arguments function)" << endl;
    return 0;
}
```

---

---

## **_53.) tutorial_21 of C/C++_**

### [**_Click me_**](tutorial_21.cpp "Clike here to see full file") to see full file of tutorial_21

```C++
// Date 31-05-2021

#include <iostream>

using namespace std;

class employee
{
private:
    int a, b, c;
    void print_all_info_function_is_in_private()
    {
        cout << "print all info Function which located in Private Function; Value of a is " << a << endl;
        cout << "print all info Function which located in Private Function; Value of b is " << b << endl;
        cout << "print all info Function which located in Private Function; Value of c is " << c << endl;
        cout << "print all info Function which located in Private Function; Value of d is " << d << endl;
        cout << "print all info Function which located in Private Function; Value of e is " << e << endl;
    }

public:
    int d, e;
    void personal_info(int a1, int b1, int c1);
    void print_all_info()
    {
        cout << "Value of a is " << a << endl;
        cout << "Value of b is " << b << endl;
        cout << "Value of c is " << c << endl;
        cout << "Value of d is " << d << endl;
        cout << "Value of e is " << e << endl;
    }

    void call_private_function() { print_all_info_function_is_in_private(); }
};

void employee::personal_info(int a1, int b1, int c1)
{
    a = a1;
    b = b1;
    b = b1;
    c = c1;
}
int main()
{
    employee aman;

    //* aman.a = 45; //This will throw an error because in class employee we had declared a in private specifiers we need to access there values from in-class declared functions in order to change their values
    //* aman.b = 14; //This will throw an error because in class employee we had declared b in private specifiers we need to access there values from in-class declared functions in order to change their values
    //* aman.c = 78; //This will throw an error because in class employee we had declared c in private specifiers we need to access there values from in-class declared functions in order to change their values

    aman.d = 9;
    aman.e = 5;
    aman.personal_info(45, 14, 78);

    aman.print_all_info();

    aman.call_private_function();
    return 0;
}
```

---

---

## **_54.) tutorial_22 of C/C++_**

### [**_Click me_**](tutorial_22.cpp "Clike here to see full file") to see full file of tutorial_22

```C++
// Date 03-06-2021

#include <iostream>
// #include <string>

using namespace std;
class binary
{
private:
    string str;
    void check_binary_or_not(void);

public:
    void read_binary(void);
    void binary_0_1_position_interchange(void);
};

void binary ::read_binary(void)
{
    cout << "Enter a number to check it is a binary number or not!" << endl;
    cin >> str;
}

void binary ::check_binary_or_not(void)
{
    for (int i = 0; i < str.length(); i++)
    {
        if (str.at(i) != '0' && str.at(i) != '1')
        {
            cout << str << " is not a Binary number!" << endl
                 << "Please enter an another number" << endl;
            exit(0);
        }
        // else if (i <= str.length())
        // {
        //     cout << str << " is a Binary number!" << endl;
        //     exit(0);
        // }
    };
}

void binary ::binary_0_1_position_interchange(void)
{
    check_binary_or_not();
    string str_copy = str;
    for (int i = 0; i < str.length(); i++)
    {

        if (str.at(i) == '0')
        {
            str.at(i) = '1';
        }
        else
        {
            str.at(i) = '0';
        }
    };
    cout << str_copy << " changed into " << str << endl;
}
int main()
{
    binary b;
    b.read_binary();
    //* b.check_binary_or_not();
    b.binary_0_1_position_interchange();

    return 0;
}
```

---

---

## **_55.) tutorial_23 of C/C++_**

### [**_Click me_**](tutorial_23.cpp "Clike here to see full file") to see full file of tutorial_23

```C++
// Date 03-06-2021

#include <iostream>

using namespace std;

class shop
{
    int item_id[100], item_price[100], counter;

public:
    void counter_value_changer(void) { counter = 0; }
    void set_item_information(void);
    void display_item_information(void);
};
void shop::set_item_information(void)
{
    cout << "Please enter item id for item " << counter + 1 << "!" << endl;
    cin >> item_id[counter];
    cout << "Please enter item price for item " << counter + 1 << "!" << endl;
    cin >> item_price[counter++];
}

void shop::display_item_information(void)
{
    for (int i = 0; i < counter; i++)
    {
        cout << "Price of item id " << item_id[i] << " is " << item_price[i] << endl;
    }
}

int main()
{
    // cout << "Hello Aman!" << endl;
    shop s;
    s.counter_value_changer();
    s.set_item_information();
    s.set_item_information();
    s.display_item_information();

    return 0;
}
```

---

---

## **_56.) tutorial_24_1 of C/C++_**

### [**_Click me_**](tutorial_24_1.cpp "Clike here to see full file") to see full file of tutorial_24_1

```C++
// Date 03-06-2021

#include <iostream>

using namespace std;

class employee
{
    int employee_id;
    static int count;

public:
    void data_taker(void)
    {
        cout << "Enter Employee for Employee number " << count + 1 << endl;
        cin >> employee_id;
        count++;
    }
    void show_employee_info(void)
    {

        cout << "Employee id for Employee number " << count << " is " << employee_id << endl;
    }
};
int employee::count;

int main()
{
    // cout << "Hello Aman!" << endl;
    employee aman, rohit;
    // aman.show_employee_info();
    aman.data_taker();
    rohit.data_taker();
    aman.show_employee_info();
    rohit.show_employee_info();
    return 0;
}
```

---

---

## **_57.) tutorial_24_2 of C/C++_**

### [**_Click me_**](tutorial_24_2.cpp "Clike here to see full file") to see full file of tutorial_24_2

```C++
// Date 03-06-2021

#include <iostream>

using namespace std;

class employee
{
    int employee_id;
    static int count;

public:
    void data_taker(void)
    {
        cout << "Enter Employee id for Employee number " << count + 1 << endl;
        cin >> employee_id;
        count++;
    }
    void show_employee_info(void)
    {

        cout << "Employee id for Employee number " << count << " is " << employee_id << endl;
    }
    static void show_count(void)
    {
        //* The Below line will throw an Error
        //! cout << id;
        //* The Above line will throw an Error
        cout << "For Employee number " << count + 1 << endl;
    }
};
//* The Below line is very import
int employee::count; //* Default value of static variable is 0
//* The Above line is very import

int main()
{
    // cout << "Hello Aman!" << endl;
    employee aman, rohit;
    // aman.show_employee_info();
    aman.show_count();
    aman.data_taker();
    rohit.show_count();
    rohit.data_taker();

    aman.show_employee_info();
    rohit.show_employee_info();
    return 0;
}
```

---

---

## **_58.) tutorial_25_1 of C/C++_**

### [**_Click me_**](tutorial_25_1.cpp "Clike here to see full file") to see full file of tutorial_25_1

```C++
// Date 05-06-2021

#include <iostream>

using namespace std;

class emoloyee
{
    int salary;
    int id;

public:
    void set_id(void)
    {
        salary = 1000;
        cout << "What is the id of the employee!" << endl;
        cin >> id;
    }
    void get_id(void)
    {
        cout << "Id is! " << id << endl
             << "Salary is! " << salary << endl;
    }
};

int main()
{

    emoloyee company[4];

    for (int i = 0; i < 5; i++)
    {
        company[i].set_id();
        company[i].get_id();
    }

    return 0;
}
```

---

---

## **_59.) tutorial_25_2 of C/C++_**

### [**_Click me_**](tutorial_25_2.cpp "Clike here to see full file") to see full file of tutorial_25_2

```C++
// Date 05-06-2021

#include <iostream>

using namespace std;

class complex
{
    int a;
    int b;

public:
    void setData(int v1, int v2)
    {
        a = v1;
        b = v2;
    }

    void setDataBySum(complex o1, complex o2)
    {
        a = o1.a + o2.a;
        b = o1.b + o2.b;
    }

    void printNumber()
    {
        cout << "Your complex number is " << a << " + " << b << "i" << endl;
    }
};

int main()
{
    complex c1, c2, c3;
    c1.setData(1, 2);
    c1.printNumber();

    c2.setData(3, 4);
    c2.printNumber();

    c3.setDataBySum(c1, c2);
    c3.printNumber();
    return 0;
}

```

---

---
