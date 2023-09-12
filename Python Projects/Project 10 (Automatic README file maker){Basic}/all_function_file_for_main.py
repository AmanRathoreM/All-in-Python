# Date 27-06-2021

from mdutils.mdutils import MdUtils


def readme_constructor(file_name="README", main_title="This is a Main Title", code_file_names_list=["check_1.py"], which_type_of_code_file_it_is="python"):

    main_title = f"<h1 style=\"text-align:center; font-size:360%; font-family:verdana;color:#4A3E76;\"><em>{main_title}</em></h1>"
    mdFile = MdUtils(file_name=file_name, title=main_title, author="Aman")

    mdFile.write('# These tutorials are watched from [**_Indian AI Production_**](https://www.youtube.com/channel/UCNzs7V6xG5GO0i_i6Grojyw "Clike here to checkout his channel") YouTube channel from [**_Seaborn Playlist_**](https://youtube.com/playlist?list=PLfP3JxW-T70HaBYwsSDadlS3v2VeALgYh "Clike here to check out his Seaborn tutorials Playlist")\n')

    mdFile.write(5*'---\n')

    i = 0
    while i < len(code_file_names_list):
        try:
            file_code = open(f"{code_file_names_list[i]}", 'r').read()
            # mdFile.write("<br>")
            mdFile.write(f"## **_{code_file_names_list[i]}_**\n")
            mdFile.write(
                f"### [**_Click me_**]({code_file_names_list[i]} \"Clike here to see full file\") to see full file of {code_file_names_list[i]}\n")

            mdFile.write(
                f"```{which_type_of_code_file_it_is}\n{str(file_code)}\n```\n")
            mdFile.write(2*'---\n')
        except Exception as e:
            print(
                f"There is no such file named \"{code_file_names_list[i]}\" or the problem is the following\n{e}")
        i += 1

    mdFile.create_md_file()


if __name__ == '__main__':
    readme_constructor(code_file_names_list=['all_function_file_for_main.py', 'check_1.py', 'check_10.py', 'check_11.py', 'check_12.py', 'check_13.py', 'check_14.py', 'check_15.py', 'check_16.py', 'check_17.py',
                       'check_18.py', 'check_19.py', 'check_2.py', 'check_20.py', 'check_3.py', 'check_4.py', 'check_5.py', 'check_6.py', 'check_7.py', 'check_8.py', 'check_9.py', 'main.py'])
