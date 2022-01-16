def fun(s):
    try:
        sample = s.split("@")
        name = sample[0]
        name_of_the_site = sample[1]
        site = name_of_the_site.split(".")
        site_name = site[0]
        site_exe = site[1]
    except ValueError:
        return False
    
    if name.replace("-", "").replace("_", "").isalnum() is False:
        return False
    elif site_name.isalnum() is False:
        return False
    elif len(site_exe) > 3:
        return False
    else:
        return True