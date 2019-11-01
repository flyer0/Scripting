<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
   xmlns:xsl="http://www.w3.org/1999/XSL/Transform" >

<xsl:output method="text" />

<xsl:template match="/">
  <xsl:apply-templates 
      select="/sales/products/record/cust/prodsale" />
</xsl:template>

<xsl:template match="prodsale">   
  <!--processing for each sale-->
  <xsl:choose>
<<<<<<< HEAD
    <xsl:when test=". >= 100">
=======
    <xsl:when test=". >= 10">
>>>>>>> 6ce10cec7fbee74221b3a548a5a4f06da9a2fca6
      <xsl:value-of select="../@num"/> <!--use parent's attr-->
      <xsl:text> - </xsl:text>
      <xsl:value-of select="id(@idref)"/> <!--go indirect-->
      <xsl:text> - </xsl:text>
      <xsl:value-of select="."/>
      <xsl:text>
</xsl:text>
    </xsl:when>
  </xsl:choose>
</xsl:template>  

</xsl:stylesheet>
