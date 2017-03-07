#!/usr/bin/python

class ResumeSection:
	'''A section within my Resume'''
	
	def __str__(self):
		return '\n'+self.text+' '+str(self.info)

	def __init__(self, **kwargs):
		self.text = ''
		self.info = ''
		if kwargs['text'] != None:
			self.text = kwargs['text']
		if kwargs['info'] != None:
			self.info = kwargs['info']
			

class Resume:

	my_resume="Ammad's Resume"
	
	@staticmethod
	def get_phone_number():
		return "313-559-5820"
	
	def __str__(self):
		return "\n(RESUME DETAILS)"+'\n\n'+self.Name + '\n'+self.Position+'\n'+self.date+'\n' +str(self.resumeinfo())+'\n'
	def __init__(self,**kwargs):
		self.Name=''
		self.Position=''
		self.date=''
		self.resume_sections=[]
		
	def add_resume_section(self,resume_addition):
		self.resume_sections.append(resume_addition)
		
	def resumeinfo(self):
		strres=""
		for item in self.resume_sections:
			strres='\n'+item.text+" : "+item.info+"\n"+strres
		return strres
		
resume=Resume()
resume.Name="Ammad Anjum Chaudhry"
resume.Position="Software Developer"
resume.date="3/6/2017"

resume_section=ResumeSection(text='About Me',info='I am a great developer that learns quick!')
resume.add_resume_section(resume_section)

print(resume)
	