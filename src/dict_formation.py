def dict_formation(d:dict):
    '''
    dict={"A":["name",moles,"state"],"B":["name",moles,"state"],...}
    Функция вернет строку с форматированием + забьет моли если они нули + вернет 2 листа вида ['name',moles,state] [...] где листы разделены по принципу A+B=C+D-> A+B->list1 C+D->list2
    '''
    