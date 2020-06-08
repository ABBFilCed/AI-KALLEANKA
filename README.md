# Kalle anka AI

Detta projekts mening var att byta ut texten i pratbubblorna på kalleankatidningar mot annan autogenererad text.
Detta mål är något jag inte lyckats uppnå men jag tänker ändå gå igenom hur det var menat att gå till.

## Pratbubblor
Först och främst var meningen att träna en AI till att känna igen pratbubblor. Till detta använde jag metoden YOLO (You Only Look Once)
Inspiration fick jag [Härifrån](https://colab.research.google.com/drive/1WHguFsueli-kBhyfcb5dDnZ66urTlFXU) och [Härifrån](https://github.com/abbjoafli/ComputerVision#train-yolo2-with-custom-objects).
Jag gjorde mitt eget dataset med pratbubblor med hjälp av denna [Guide](https://medium.com/@manivannan_data/yolo-annotation-tool-new-18c7847a2186). Detta är colaben för [Yolo pratbubblor](https://colab.research.google.com/drive/1Ed3q4sc2p9-_cFtjLg36hT-BOalslfdx#scrollTo=sx6mR4m2vAMb)


## Textigenkänning
I det här projektet behövde jag använda mig av två olika textigenkännings eller OCR metoder.

### 1.
Den första var till för att ta fram texten ur pratbubblorna ur ett en del tidningar för att kunna använda denna text som träningsdata till programmet som skulle auto generera den nya texten.
Här är länken till denna github finns [här](https://github.com/jbarlow83/OCRmyPDF).
Det detta program ska göra är att ta ut texten ur en bild och lägga den i ett pdf dokument. Hur detta dokument skulle användas kommer vi gå igenom senare

### 2.
En annan metod behövde användas för att hitta texten i tidningen som matas in av användaren. För detta försökte jag med flera olika metoder men ingen tycktes förstå typsnittet i kalleanka tidningarna. 

## Textgenerering
Som nämnt tidigare tänkte jag använda en AI för att generera ny text till pratbubblorna. Inspiration till denna AI fick jag [härifrån](https://colab.research.google.com/drive/1E7A_sKswEkeaYup2vAZGyjSPkzyVSEbj). Träningsdatan till denna AI skulle vara texten som togs fram av den första OCR metoden. 

## Sammanställning
Programmet i helhet skulle fungera på ett sådant sätt att man matade in en sida ur eller en hel kalleanka tidning. Sedan användes Yolo tränad på pratbubblorna till att ta reda på var i bilden pratbubblorna var. Detta gjordes innan textigenkänningen eftersom jag inte ville byta ut annan text än den i pratbubblorna då jag tror att detta hade försämrat resultatet. Därefter skulle OCR metod två användas för att ta reda på vart det fanns text i pratbubblorna och dessa områden skulle maskeras över med vitt. Sedan skulle ny autogenerarad text placeras ovanpå dessa vita lager.

## Samanfattning
Som sagt blev jag inte färdig med hela detta projekt men jag kom en bit och jag har lärt mig mycket på vägens gång.
Skulle jag göra om projektet skulle jag ha gjort ett projekt som involverade färre delar eller i alla fall flera delar som kunde agera självständigt så att det inte gjort lika mycket om jag misslyckats med någon del. När man håller på med sådana här projekt är man väldigt beroende på andras arbete eftersom det skulle vara så gott som omöjligt att göra detta från scratch på tiden som var tillgänglig. Ibland får man detta att fungera utmärkt och ibland gör man det inte och detta råkade vara en av gångerna då det inte gjorde det.
