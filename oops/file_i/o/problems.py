class employee():
    name="none"
    lang="py"
    sal=1200000
    def __init__(self,name,lang,sal):
        self.name=name
        self.lang=lang
        self.sal=sal
        
s=employee("srajal","py",1500000)
print(s.name,s.lang,s.sal)