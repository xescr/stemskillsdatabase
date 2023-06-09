# Importing Pandas to create DataFrame
import pandas as pd
import random
import ast
# Creating Empty DataFrame and Storing it in variable df


def init_database():
    df = pd.DataFrame(columns=['Names', 'Skills', 'Projects Completed', 'Projects In progress', 'UUID', 'YEAR'])

    # Printing Empty DataFrame For Debugging Purposes
    df.to_csv("database.csv", index=False)


def get_userdata(uuid):
    df = pd.read_csv("database.csv", index_col=False)
    list = df.UUID.values.tolist()
    print(uuid)
    print(list)
    print(list[0])

    if int(uuid) in list:
        print("checkpoint")
        index = df.UUID[df.UUID == int(uuid)].index.tolist()[0]
        print(index)
    else:
        return 0
    row_object = df.loc[index]
    return row_object


def init_user_exact(name, competency, finished_projects, underway_projects, uuid, year):
    # When I get the nfc tags and stuff I'll probably make it randomize a UUID and
    # write it to the nfc tag at this point

    # Something like uuid = random.randint(100000, 999999)

    df = pd.read_csv("database.csv", index_col=False)
    df.loc[len(df)] = [name, competency, finished_projects, underway_projects, uuid, year]
    df.to_csv("database.csv", index=False)


def init_user_random(class_list, year):
    df = pd.read_csv("database.csv", index_col=False)
    num = random.randint(1000000, 9999999)
    num_list = []
    for student in class_list:
        while num in df['UUID'].values:
            num = random.randint(1000000, 9999999)
        df.loc[len(df)] = [student, None, None, None, num, year]
        num_list.append(num)
    print(df.to_string())
    df.to_csv("database.csv", index=False)
    return num_list



        #print(num)
        #print(df.to_string())


def add_skill(skill, uuid):
    df = pd.read_csv("database.csv", index_col=False)
    try:
        old_value_string = (df['Skills'][df['UUID'] == uuid].values[0])
    except:
        old_value_string = 1947

    if not isinstance(old_value_string, str):
        current_value = f'{{"{skill}": 1}}'
    else:
        current_value = ast.literal_eval(old_value_string)
        if skill in current_value:
            if current_value[skill] >= 4:
                pass
            else:
                current_value[skill] = current_value[skill] + 1
        else:
            current_value.update({skill: 1})
    # Selects value in row where UUID column equals param
    # And the column is equal to skills, then assigns to
    # Current value
    """print(current_value)"""
    # Finds the index of the aforementioned row
    index = df.UUID[df.UUID == uuid].index.tolist()[0]
    current_value_string = str(current_value)
    df.at[int(index), 'Skills'] = current_value_string
    df.to_csv("database/database.csv", index=False)
    return get_userdata(uuid)


def add_project(project, uuid):
    df = pd.read_csv("database.csv", index_col=False)
    try:
        old_value_string = (df['Projects Completed'][df['UUID'] == uuid].values[0])
    except:
        old_value_string = 1947
    if not isinstance(old_value_string, str):
        current_value = f'["{project}"]'
    else:
        current_value = ast.literal_eval(old_value_string)
        if project in current_value:
                pass
        else:
            current_value.append(project)
    # Selects value in row where UUID column equals param
    # And the column is equal to skills, then assigns to
    # Current value
    """print(current_value)"""
    # Finds the index of the aforementioned row
    index = df.UUID[df.UUID == uuid].index.tolist()[0]
    current_value_string = str(current_value)
    df.at[int(index), 'Projects Completed'] = current_value_string
    df.to_csv("database/database.csv", index=False)
    return get_userdata(uuid)


def add_project_progress(project, uuid):
    df = pd.read_csv("database.csv", index_col=False)
    try:
        old_value_string = (df['Projects In Progress'][df['UUID'] == uuid].values[0])
    except:
        old_value_string = 1947
    if not isinstance(old_value_string, str):
        current_value = f'["{project}"]'
    else:
        current_value = ast.literal_eval(old_value_string)
        if project in current_value:
                pass
        else:
            current_value.append(project)
    # Selects value in row where UUID column equals param
    # And the column is equal to skills, then assigns to
    # Current value
    """print(current_value)"""
    # Finds the index of the aforementioned row
    index = df.UUID[df.UUID == uuid].index.tolist()[0]
    current_value_string = str(current_value)
    df.at[int(index), 'Projects In progress'] = current_value_string
    df.to_csv("database/database.csv", index=False)

if __name__ == "__main__":
    print(get_userdata(1591797))