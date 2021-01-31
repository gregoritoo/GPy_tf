import numpy as np 
import os
import re 

def devellopement(kernel_list):
    splitted = []
    splitted_params = []
    j = 0
    first_mul = False
    for i in range(len(kernel_list)) :
        if kernel_list[i][0]=="*" :
            if j != i : 
                splitted.append(kernel_list[j:i])
                splitted_params.append([np.range(j,i+1)])
            for p in range(len(splitted)) :
                if len(splitted[p]) > 0   :
                    splitted[p].append(kernel_list[i])
                    splitted_params[p].append(i)
            j=i+1 
        else :
            splitted.append([kernel_list[i]])
            splitted_params.append([i])
            j=i+1 
    return splitted,splitted_params



def comment(text,component,pos,params_dic,list_params):
    list_of_dic = [list_params[position] for position in pos]
    for j in range(len(component)) :
        kern = component[j]
        params = list_of_dic[j]
        if re.search('\+LIN', kern) is not None :
            text =text + "\t A linear component with a offset of {:.1f} and a slope of {:.1f} , ".format(float(params_dic[params[0]]),float(params_dic[params[1]].numpy()[0])) 
        if re.search('\+SE', kern) is not None :
            text =text + "\t A smooth  function with a lengthscale of {:.1f} and a variance of {:.1f} , ".format(float(params_dic[params[0]]),float(params_dic[params[1]].numpy()[0])) 
        if re.search('\+PER', kern) is not None :
            text = text + "\t A periodic component with a period of {:.1f} , a variance of {:.1f} and lengthscale of {:.1f} , ".format(float(params_dic[params[1]].numpy()[0]),float(params_dic[params[2]].numpy()[0]),float(params_dic[params[0]].numpy()[0]))
        if  re.search('\*LIN', kern) is not None :
            if re.search('\*LIN\*LIN', kern) is not None :
                text = text + "with polynomial varying amplitude  of  {:.1f} , ".format(float(params_dic[params[0]].numpy()[0]))
            else :
                text = text + "with a linearely varying amplitude  of {:.1f} , ".format(float(params_dic[params[0]].numpy()[0]))
        if re.search('\*PER', kern) is not None :
            text = text + "modulated by a periodic function defined by a period of {:.1f}, a variance of {:.1f} and lengthscale of {:.1f} , ".format(float(params_dic[params[1]].numpy()[0]),float(params_dic[params[2]].numpy()[0]),float(params_dic[params[0]].numpy()[0]))
        if  re.search('\*SE', kern) is not None  :
            text = text + "whose shape varying smoothly with a lengthscale of {:.1f} , ".format(float(params_dic[params[0]].numpy()[0]))
    return text[:-2]+"."
    

def comment_gpy(text,component,pos,variables_names,variables):
    list_of_dic = [variables[position] for position in pos]
    for j in range(len(component)) :
        kern = component[j]
        params = list_of_dic[j]
        if re.search('\+LIN', kern) is not None :
            text =text + "\t A linear component with  a slope of {:.1f} , ".format(params[0]) 
        if re.search('\+SE', kern) is not None :
            text =text + "\t A smooth  function with a lengthscale of {:.1f} and a variance of {:.1f} , ".format(params[1],params[0]) 
        if re.search('\+PER', kern) is not None :
            text = text + "\t A periodic component with a period of {:.1f}, a variance of {:.1f} and lengthscale of {:.1f} , ".format(params[1],params[0],params[2])
        if  re.search('\*LIN', kern) is not None :
            if re.search('\*LIN\*LIN', kern) is not None :
                text = text + "with polynomial varying amplitude  of  {:.1f} , ".format(params[0])
            else :
                text = text + "with a linearely varying amplitude  of {:.1f} , ".format(params[0])
        if re.search('\*PER', kern) is not None :
            text = text + "modulated by a periodic function defined by a period of {:.1f}, a variance of {:.1f} and lengthscale of {:.1f} , ".format(params[1],params[0],params[2])
        if  re.search('\*SE', kern) is not None  :
            text = text + "whose shape varying smoothly with a lengthscale of {:.1f} , ".format(params[1],params[0])
    return text[:-2]+"."





