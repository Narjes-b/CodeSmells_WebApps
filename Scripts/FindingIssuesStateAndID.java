package Fault;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;



/**
 * @author NarjesBessghaier
 */
public class Issues {
	public static String Commit;
	public static String IssueID;
	public static void main(String[] args) throws ParserConfigurationException, SAXException, IOException  {
		// TODO Auto-generated method stub
		
		//extract commit SHA and isuueID
		
		String file2="/Users/bessghaiernarjess/Documents/PhD_ETS/Contrib1-Diffusion/Fault-proneness/CommitsWithFixedMessage.xls";
        
	     //String file="/Users/bessghaiernarjess/Desktop/about.uixFinalOutputFile.xls";
	 	InputStream input = new FileInputStream(file2);
			 HSSFWorkbook wb     = new HSSFWorkbook(input);
			 HSSFSheet sheet = wb.getSheetAt(0);
			 int rowTotal = sheet.getLastRowNum();    
				 
			 if ((rowTotal > 0) || (sheet.getPhysicalNumberOfRows() > 0)) {
		          rowTotal++;
		      }	 
			 
		String[] SHAtab= new String[rowTotal];	 
		String[] IssueIDtab= new String[rowTotal];	 
			
for ( int r=0;r<rowTotal; r++){ 
	
	//extrcat SHA :: ^.{0,8}
	
	 HSSFRow row     = sheet.getRow(r); 
	 HSSFCell cell= row.getCell(0);
	 String SHA= cell.getStringCellValue();
	 
	 
	 Pattern p = Pattern.compile("^.{0,7}");
     Matcher m = p.matcher(SHA);
     while(m.find()) {
    	 SHA=m.group();
         //System.out.println(m.group());
     }
     Commit = SHA;
     //System.out.println("Commit : " +Commit);
     SHAtab[r]=Commit;
     String issue= cell.getStringCellValue();
     
     Pattern p1 = Pattern.compile("[^#]+$"); 
     Matcher m1 = p1.matcher(issue);
     while(m1.find()) {
    	 issue=m1.group();
         //System.out.println(m.group());
     }
     
     //System.out.println("IssueID : " +issue);
    //get numeric value
     Pattern p11 = Pattern.compile("\\d+"); 
     Matcher m11 = p11.matcher(issue);
     while(m11.find()) {
    	 issue=m11.group();
         //System.out.println(m.group());
     }
	 IssueID =issue;
	 IssueIDtab[r]=IssueID;
     //System.out.println("IssueID : " +IssueID);
	 }
	  
for ( int r=0;r<rowTotal; r++){ 
	 System.out.println("SHAtab : " +SHAtab[r]);
	 System.out.println("IssueIDtab : " +IssueIDtab[r]);
}

		
		 File inputFile = new File("/Users/bessghaiernarjess/Downloads/test.xml");
        
		 DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
         DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
         Document doc = dBuilder.parse(inputFile);
         doc.getDocumentElement().normalize();
         //System.out.println("Root element :" + doc.getDocumentElement().getNodeName());
         NodeList nList = doc.getElementsByTagName("JSON_ARRAY");

         for (int temp = 0; temp < nList.getLength(); temp++) {
	            Node nNode = nList.item(temp);
	            if (nNode.getNodeType() == Node.ELEMENT_NODE) {
	               Element eElement = (Element) nNode;
	               
	               System.out.println("Root element: " + doc.getDocumentElement().getNodeName());  
	               
	               String number=  eElement.getElementsByTagName("number").item(0).getTextContent();
	               System.out.println("number = : " + number);
	              
	               NodeList listOfElement = eElement.getElementsByTagName("labels");
	               int nchild=0;
	               nchild=listOfElement.getLength();
	               for (int temp1 = 0; temp1 < nchild; temp1++) {
	            	   Node nNode1 = listOfElement.item(temp1);
	            	   if (nNode1.getNodeType() == Node.ELEMENT_NODE) {
	    	               Element children = (Element) nNode1;  
	               System.out.println("name =  : " 
	     	                  + children
	     	                  .getElementsByTagName("name").item(0).getTextContent());break;
	     	                  }}
	               String state=eElement.getElementsByTagName("state").item(0).getTextContent();
	               System.out.println("state = : " + state);
	               
	               NodeList listOfElement1 = eElement.getElementsByTagName("milestone");
	               int nchild1=0;
	               nchild1=listOfElement1.getLength();
	               String milestone=  eElement.getElementsByTagName("milestone").item(0).getTextContent();
	               if (milestone.equals("null"))
	               {
	            	   System.out.println("created_at = : " + eElement.getElementsByTagName("created_at").item(0).getTextContent());
	            	   System.out.println("closed_at = : " + eElement.getElementsByTagName("closed_at").item(0).getTextContent());
	               }
	               else {
	               for (int temp1 = 0; temp1 < nchild1; temp1++) {
	            	   Node nNode1 = listOfElement1.item(temp1);
	            	   if (nNode1.getNodeType() == Node.ELEMENT_NODE) {
	    	               Element children = (Element) nNode1;  
	               System.out.println("created_at =  : " 
	     	                  + children
	     	                  .getElementsByTagName("created_at").item(0).getTextContent());
	              
	               System.out.println("closed_at =  : " 
	     	                  + children
	     	                  .getElementsByTagName("closed_at").item(0).getTextContent());
	     	                  }}
	               }
	               
	               
	               for ( int r=0;r<rowTotal; r++){ 
	            	   if (number.equals(IssueIDtab[r]) & eElement.getElementsByTagName("name").item(0).getTextContent().equals("bug") ) 
	            	   {
	            		   System.out.println("Fault-fixing commit found" );
	            	   }
	            	}
	             
	               
	               
	               // git log --oneline | grep 'fixe'
	              // curl https://api.github.com/repos/composer/composer/issues?state=closed     &page=1
	               
	               
	               
	               
	               
	               
	               
	               
	            }}
	
	
	}

}
