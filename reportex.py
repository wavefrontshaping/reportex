#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:32:54 2018

@author: spopoff
"""

#%%

import os,shutil
import subprocess
import re
#from inspect import getsourcefile
#from os.path import abspath

#print(os.path.abspath(getsourcefile(lambda:0)))
#print(__file__)

class report():
    
    def __init__(self,template):
        
        assert(not os.path.exists('temp_latex'))
        
        self.template_folder = os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'templates',
                template)
       
        path_to_template = os.path.join(
                self.template_folder,
                'template.tex')
#        print(path_to_template)
        with open(path_to_template) as tex_file:
            self.content = tex_file.read()
            # remove comments
            self.content = re.sub(r"(\%+(?:[^(\%\n].*\n|\n))",'',self.content)
#            print(self.content)
            
        self.document_data = {'document_title': '',
                              'document_subtitle': '',
                              'main_text': ''
                              }
        self.num_fig = 0
#        self.title = ''
#        self.subtitle = ''
#        self.mainText = ''
           

    def setTitle(self,title,subtitle):
        self.document_data['document_title'] = title
        self.document_data['document_subtitle'] = subtitle
#         self.title = title
#         self.title = subtitle
        
    def createTempFolder(self):
        if not os.path.exists('temp_latex'):
            os.makedirs('temp_latex')
  
    def addText(self,text):
#        self.mainText = '%s\n%s' % (self.mainText,text)
        self.document_data['main_text'] =  '%s\n%s' % (self.document_data['main_text'],text)
        
    def cleanText(self,string):
        return ("%r"%string)[1:-1]
        
    
    def addFig(self,fig,caption = '', width = "0.8\textwidth",dpi = 200,label=''):
        self.createTempFolder()
        self.num_fig+=1
        fig.savefig(os.path.join('temp_latex','fig_%g.eps' % self.num_fig), format='eps', dpi=dpi)
        print(self.cleanText(width))
        self.addText(
                r''' 
                \begin{figure}[ht]
                \centering
                \includegraphics[width=%s]{%s}
                \caption{%s}
                \label{%s}
                \end{figure}''' %
                (
                 self.cleanText(width),
                 'fig_%g.eps' % self.num_fig,
                 self.cleanText(caption),
                 self.cleanText(label)
                )
                
                )
        
    def generatePDF(self,path_out):
        
        # create temporary folder if ot already done
        self.createTempFolder()
        
        # generate the text
        text_tex = self.content % self.document_data
        
        
        
        if os.path.exists(os.path.join(self.template_folder,'data')):
            shutil.copytree(os.path.join(self.template_folder,'data'), 'temp_latex/data')
        # write latex file
#        with open(path_out+'.tex', 'w') as out_file:
        temp_latex_path = os.path.join('temp_latex','reportex.tex')
        with open(temp_latex_path, 'w') as out_file:    
            out_file.write(text_tex)

        os.chdir('temp_latex')

        # compile pdf
        cmd = ['pdflatex', '-interaction', 'nonstopmode', 'reportex.tex']
#        cmd = ['pdflatex', '-output-directory', 'temp_latex',  temp_latex_path]
        print(cmd)
        proc = subprocess.Popen(cmd)
        proc.communicate()
        
        os.chdir('..')
                
        retcode = proc.returncode
        if not retcode == 0:
#            os.unlink(path_out+'.pdf')
#            shutil.rmtree('temp_latex')
            raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd))) 
        
        # copy the pdf to the output desired location
        shutil.move(os.path.join('temp_latex','reportex.pdf'),path_out+'.pdf')
        
#         remove temporary files
        shutil.rmtree('temp_latex')
