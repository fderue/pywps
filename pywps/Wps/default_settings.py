"""
This is default main configuration file for pywps. Do NOT change this file,
unless you do not know, what you are doing. For custom changes, copy this
file as pywps/etc/settigs.py and change the variables there.

The most importand parts are
WPS[ServiceIdenteification]
ServerSettings
"""
# Author:	Jachym Cepicky
#        	http://les-ejk.cz
# Lince: 
# 
# Web Processing Service implementation (conf. file)
# Copyright (C) 2006 Jachym Cepicky
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA



###########################################################
#
# In this WPS structure the main configuration is stored
#
# DO NOT CHANGE THIS
#
###########################################################
WPS = {
    # version of supported WPS
    # 'version':"0.4.0"
    'version': "0.4.0",

    # encoding of output XMLs
    # 'encoding': "utf-8",
    'encoding': "utf-8",

    # debuging 
    # "debug": False
    "debug": False,

    #
    # This are mandatory and optional conf. parameters
    #
    'ServiceIdentification': {

        ####################
        # Mandatory options
        ####################
        #
        # 'Title':"This WPS Title",
        #
        'Title':"PyWPS 2.0.0",
        #
        # 'ServiceType":"WPS",
        #
        'ServiceType':"WPS",
        #
        # 'ServiceTypeVersion':"1.0.0",
        #
        'ServiceTypeVersion':"1.0.0",

        ####################
        # Optional options
        ####################
        #
        #'Abstract':'Abstract to this WPS',
        #
        #
        #'Fees':'$0',
        #
        #
        #'AccesConstraints':'',
        #
    },
    
    #
    # Service provider identification
    #
    'ServiceProvider': {
            'ProviderName' : "Your Company Name",
            'IndividualName':"Your Name",
            'PositionName':"Your Position",
            'Role':"Your role",
            'DeliveryPoint': "Street ",
            'City': "City",
            'PostalCode':"000000",
            'Country': "Your Country",
            'ElectronicMailAddress':"your@email.address.org",
    },

    # 
    # OperationsMetadata options
    #
    'OperationsMetadata': {
        #
        # ServerAddress - URL address to your pywps server
        #'ServerAddress' : "http://localhost/cgi-bin/wps/wps.py",
        'ServerAddress' : "http://localhost/cgi-bin/wps/wps.py",
    },

    #
    # Server Keywords array
    # 
    # 'Keywords': ['GRASS','GIS','WPS'],
    'Keywords' : ['GRASS','GIS','WPS'],

}

###########################################################
#
# In this ServerSettings structure, the most importand server settings are
# stored
#
###########################################################
ServerSettings = {
    #
    # outputPath - directory, where your files will be stored, if
    # storeSupported is set to "true"
    # NOTE: You have to create this directory manualy and set rights, so
    #       the program is able to store data in there 
    # 'outputPath':'/var/www/wpsoutputs',
    'outputPath': '/var/www/wps/wpsoutputs/',
    
    #
    # 'outputUrl' - URL of the directory, where the outputs will be stored
    # 'outputUrl': 'http://localhost/wpsoutputs',
    'outputUrl':  'http://localhost/wps/wpsoutputs',

    #
    # tempPath - path to directory, where temporary data will be stored.
    # NOTE: the pywps has to have rights, to create directories and files
    #       in this directory
    # 'tempPath':'/tmp',
    'tempPath': '/tmp',

    #
    # maxOperations - maximum number of operations, which is allowed to low
    # on this server at ones 
    # default = 1
    # 'maxOperations':1,
    'maxOperations':1,
    
    #
    # maxSize: maximum input file size in bytes
    # NOTE: maximum file size is 5MB, no care, if this number is heigher
    # 'maxSize':5242880, # 5 MB
    'maxSize':5242880, # 5 MB

    #
    # maxInputParamLength: maximal length of input values
    # NOTE: maximal length of input parameters is 256, no mather, how height
    #       is this number
    # 'maxInputParamLength':1024,
    'maxInputParamLength':1024,
}
