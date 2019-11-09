<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0">
    xmlns:xsl ='http://www.w3.org/1999/XSL/Transform'>


<xsl:template match='/'>
    <xsl:for-ech select='//product'>
    <xsl:variable name='pid' select '@id'/>
        <xsl:value-of select='.'/><xsl:text> : </xsl:text>
        <xsl:value-of select='sum(//prodsale[@idref=$pid])' /><xsl:text>
        </xsl:text>
    </xsl:for-each>
</xsl:template>