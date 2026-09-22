#to do list
print("MENU:")
print("    TO DO LIST  ")
print("1-Add task")
print("2-Remove task")
print("3-View tasks")
print("4-Update")
print("5-View progress")
print("6-Exit")
task_list=list()
choice=0
complete=0
while choice!="6":
    choice=input("enter your choice: ")
    if(choice=="1"):
      q1=int(input("how many tasks you want to add?"))
      for i in range(q1):
       task=input("Enter task: ").lower()
       if(task not in task_list ):
         task_list.append(task)
       else:
         print("Task is already present in list")
    elif(choice=="2"):
      task=input("Enter task that you want to remove from list: ").lower()
      if(task  in task_list):
        task_list.remove(task)
        print("List after")
        for index,i in enumerate(task_list):
                      index+=1
                      print(index,i)
      else:
        print("this task is not present in list ")
     
    elif(choice=="3"):
      for index,i in enumerate(task_list):
        index+=1
        print(index,"-",i)
    elif(choice=="4"):
       text=""
       while text.lower()!="done":
         text=input("enter number that you have completed(enter done after completion)")
         if(text=="done"):
          break
         index=int(text)-1
         if(index>=0 and index<len(task_list)):
          if("Completed" not in task_list[index]):
           task_list[index]=task_list[index].replace(task_list[index], task_list[index]+" Completed")      
           complete+=1
          else:
            print("It's already completed")
         else:
            print("invalid index")
       for index,i in enumerate(task_list):
                      index+=1
                      print(index,i)
    elif(choice=="5"):
     if(len(task_list)!=0):
      print("Progress")
      print(complete/len(task_list)*100,"%")
     else:
        print("No task in list")
    elif(choice=="6"):
        break
    else:
        print("invalid command ")
print("GoodBye")
      