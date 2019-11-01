<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0">
    xmlns:xsl ="http://www.w3.org/1999/XSL/Transform">
    
<xsl:template match="//energieverbrauch">
<xsl:variable name="e" select ="energietraeger[bezeichnung = 'Brennstoffe ']"/>
<xsl:choose> 
<xsl:when test ="$e">
<xsl:value-of select ="$e/wert"/>
</xsl:when>
</xsl:choose >
</xsl:template >
</xsl:stylesheet>
