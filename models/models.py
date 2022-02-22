"Models for Modeladmin"
from django.db import models

class TrainingModel(models.Model):
    description = models.CharField(max_length=200)
    date = models.DateTimeField('date created')
    hostname = models.CharField(max_length=40)
    history_path = models.CharField(max_length=200)
    model_path = models.CharField(max_length=200)
    figures_dir = models.CharField(max_length=200)
    dict_text_output_path = models.CharField(max_length=200)
    checkpoint_path = models.CharField(max_length=200)
    test_indexes_list_path = models.CharField(max_length=200)
    test_indexes_list_path = models.CharField(max_length=200)
    imagecount = models.IntegerField()
    num_training_img = models.IntegerField()
    num_validation_img = models.IntegerField()
    epocs = models.IntegerField()
    batch_size = models.IntegerField()
    loss = models.CharField(max_length=20)
    metrics = models.CharField(max_length=20)
    optimizer = models.CharField(max_length=20)
    power = models.IntegerField()
    n_blocks = models.IntegerField()
    normalization = models.CharField(max_length=20)
    learning_rate = models.FloatField()


# {'loss': [0.0163359884172678, 0.008184543810784817, 0.0071385265327990055, 0.005776355043053627, 0.007443602196872234, 0.0056756362318992615, 0.0046767182648181915, 0.005099080502986908, 0.004132102709263563, 0.0038907534908503294, 0.0035459573846310377, 0.0033840369433164597, 0.0032344490755349398, 0.003123851493000984, 0.0030015655793249607, 0.0029384219087660313, 0.002816307358443737, 0.002746117999777198, 0.00290345074608922, 0.0026318731252104044, 0.0025261002592742443, 0.0024772845208644867, 0.0024610748514533043, 0.0023359041661024094, 0.002281360561028123, 0.0022423795890063047, 0.002520246198400855, 0.003135680453851819, 0.0034412816166877747, 0.0026953958440572023, 0.002479010261595249, 0.0023414765018969774, 0.0020491895265877247, 0.0019838837906718254, 0.0019431161927059293, 0.001904736622236669, 0.0018710260046646, 0.0018422763096168637, 0.0018129755044355989, 0.001788423745892942, 0.0017622950254008174, 0.0017392316367477179, 0.001717980019748211, 0.001698660315014422, 0.001677122781984508, 0.0016604432603344321, 0.0016415759455412626, 0.0015556378057226539, 0.0015324599808081985, 0.0015258144121617079, 0.0015189626719802618, 0.0015110108070075512, 0.0015057064592838287, 0.001502008643001318, 0.0014927054289728403, 0.001490199938416481, 0.0014802932273596525, 0.0014789802953600883, 0.0014742609346285462, 0.0014676760183647275, 0.0014658337458968163, 0.0014585541794076562, 0.0014397462364286184, 0.0014386314433068037, 0.00143571721855551, 0.0014316922752186656, 0.001430910313501954, 0.0014299858594313264, 0.0014324570074677467, 0.0014277820009738207, 0.00142769911326468, 0.0014282753691077232, 0.0014257309958338737, 0.0014248659135773778, 0.001422043889760971, 0.001422387664206326, 0.0014211746165528893, 0.0014173820381984115, 0.0014187453780323267, 0.0014165713218972087, 0.0014153227675706148, 0.001416796469129622, 0.0014168036868795753, 0.0014147799229249358, 0.0014143387088552117, 0.00141514849383384, 0.0014150550123304129, 0.0014183551538735628, 0.001412716694176197, 0.0014140765415504575, 0.0014142983127385378, 0.0014135270612314343, 0.0014133101794868708, 0.0014130780473351479, 0.0014112894423305988, 0.0014121978310868144, 0.0014123745495453477, 0.0014131262432783842, 0.0014129261253401637, 0.0014114056248217821], 'mse': [0.01633596420288086, 0.008184542879462242, 0.007138522807508707, 0.0057763587683439255, 0.007443594746291637, 0.005675638560205698, 0.004676716402173042, 0.005099080502986908, 0.004132094793021679, 0.0038907600101083517, 0.0035459615755826235, 0.003384035313501954, 0.003234450239688158, 0.003123851027339697, 0.003001563483849168, 0.0029384170193225145, 0.002816308056935668, 0.002746120560914278, 0.002903450047597289, 0.0026318724267184734, 0.0025261002592742443, 0.0024772868491709232, 0.0024610739201307297, 0.0023359081242233515, 0.0022813614923506975, 0.002242378192022443, 0.0025202485267072916, 0.00313568115234375, 0.0034412825480103493, 0.002695393282920122, 0.0024790081661194563, 0.0023414716124534607, 0.00204918859526515, 0.0019838851876556873, 0.001943118404597044, 0.001904735341668129, 0.0018710277508944273, 0.0018422777066007257, 0.0018129769014194608, 0.0017884242115542293, 0.0017622956074774265, 0.001739232218824327, 0.0017179795540869236, 0.0016986633418127894, 0.0016771249938756227, 0.001660442678257823, 0.0016415780410170555, 0.0015556388534605503, 0.0015324600972235203, 0.0015258151106536388, 0.0015189640689641237, 0.001511011621914804, 0.0015057059936225414, 0.0015020081773400307, 0.0014927060110494494, 0.0014902027323842049, 0.0014802936930209398, 0.0014789828564971685, 0.0014742614002898335, 0.0014676747377961874, 0.001465833862312138, 0.00145855569280684, 0.0014397460035979748, 0.0014386298134922981, 0.00143571593798697, 0.0014316922752186656, 0.001430910313501954, 0.0014299857430160046, 0.001432457473129034, 0.001427781768143177, 0.0014277006266638637, 0.0014282723423093557, 0.0014257311122491956, 0.0014248655643314123, 0.001422045985236764, 0.001422386965714395, 0.0014211763627827168, 0.0014173822710290551, 0.0014187464257702231, 0.0014165685279294848, 0.0014153213705867529, 0.0014167969347909093, 0.001416803919710219, 0.001414778525941074, 0.0014143397565931082, 0.0014151486102491617, 0.0014150561764836311, 0.0014183548046275973, 0.0014127178583294153, 0.0014140777057036757, 0.0014142990112304688, 0.0014135271776467562, 0.0014133091317489743, 0.0014130781637504697, 0.0014112910721451044, 0.001412197481840849, 0.0014123733853921294, 0.0014131248462945223, 0.0014129255432635546, 0.0014114053919911385], 'val_loss': [0.015462156385183334, 0.01483288872987032, 0.013264668174088001, 0.014106807298958302, 0.014568869024515152, 0.012280588038265705, 0.012015735730528831, 0.013393141329288483, 0.010870919562876225, 0.010948005132377148, 0.010784938000142574, 0.010184154845774174, 0.01015077717602253, 0.011298944242298603, 0.010356995277106762, 0.010449978522956371, 0.010008752346038818, 0.009999570436775684, 0.010441040620207787, 0.010435672476887703, 0.010116659104824066, 0.010222776792943478, 0.010364570654928684, 0.01019927766174078, 0.01008384209126234, 0.010294473730027676, 0.30228906869888306, 0.010365219786763191, 0.0104294428601861, 0.01025138609111309, 0.010295560583472252, 0.010277274064719677, 0.010171584784984589, 0.01025408785790205, 0.01027127355337143, 0.010318680666387081, 0.01037136372178793, 0.010366149246692657, 0.010449334047734737, 0.010451490059494972, 0.010531246662139893, 0.010490639135241508, 0.010519145056605339, 0.010577023960649967, 0.010623615235090256, 0.010686596855521202, 0.010711656883358955, 0.010744364932179451, 0.010765181854367256, 0.01076631061732769, 0.01081030908972025, 0.010818726383149624, 0.010850771330296993, 0.01082833856344223, 0.010851942002773285, 0.010875899344682693, 0.010866339318454266, 0.010887304320931435, 0.010930350050330162, 0.010959223844110966, 0.010912316851317883, 0.010934705846011639, 0.01096009835600853, 0.010959441773593426, 0.010969397611916065, 0.010976262390613556, 0.010976891964673996, 0.010979052633047104, 0.010976209305226803, 0.010991902090609074, 0.010987424291670322, 0.01099253911525011, 0.010995435528457165, 0.010993210598826408, 0.010993702337145805, 0.011001607403159142, 0.01100053172558546, 0.011001038365066051, 0.011012467555701733, 0.011012143455445766, 0.01100917998701334, 0.011010298505425453, 0.011007452383637428, 0.01100901048630476, 0.011008448898792267, 0.011012009344995022, 0.0110138775780797, 0.011013111099600792, 0.011018150486052036, 0.011019748635590076, 0.011012496426701546, 0.011018889024853706, 0.011017664335668087, 0.01101695653051138, 0.01101165171712637, 0.011018355377018452, 0.011019840836524963, 0.011019024066627026, 0.011015565134584904, 0.011017564684152603], 'val_mse': [0.015462150797247887, 0.014832892455160618, 0.0132646718993783, 0.014106810092926025, 0.014568866230547428, 0.012280585244297981, 0.01201574131846428, 0.01339314691722393, 0.010870925150811672, 0.010948005132377148, 0.010784940794110298, 0.010184155777096748, 0.010150784626603127, 0.011298952624201775, 0.010356996208429337, 0.0104499701410532, 0.010008751414716244, 0.009999576024711132, 0.010441038757562637, 0.010435666888952255, 0.01011666376143694, 0.010222776792943478, 0.010364568792283535, 0.010199282318353653, 0.010083845816552639, 0.010294468142092228, 0.30228906869888306, 0.010365219786763191, 0.010429449379444122, 0.010251385159790516, 0.010295558720827103, 0.010277271270751953, 0.010171583853662014, 0.0102540859952569, 0.010271272622048855, 0.010318676941096783, 0.010371358133852482, 0.010366151109337807, 0.010449331253767014, 0.01045149378478527, 0.010531249456107616, 0.010490630753338337, 0.010519142262637615, 0.010577023029327393, 0.010623622685670853, 0.010686606168746948, 0.010711653158068657, 0.010744364932179451, 0.010765180923044682, 0.010766313411295414, 0.010810300707817078, 0.0108187235891819, 0.010850772261619568, 0.010828334838151932, 0.010851944796741009, 0.010875900276005268, 0.010866346769034863, 0.010887304320931435, 0.010930349119007587, 0.010959227569401264, 0.01091231033205986, 0.010934715159237385, 0.010960101149976254, 0.010959438979625702, 0.010969392955303192, 0.010976259596645832, 0.01097689289599657, 0.01097906194627285, 0.010976212099194527, 0.010991907678544521, 0.010987426154315472, 0.010992534458637238, 0.01099543645977974, 0.01099321711808443, 0.01099370513111353, 0.011001599952578545, 0.011000530794262886, 0.01100104209035635, 0.011012464761734009, 0.011012139730155468, 0.01100917998701334, 0.011010292917490005, 0.011007453314960003, 0.011009005829691887, 0.011008449830114841, 0.01101201307028532, 0.011013881303369999, 0.011013106442987919, 0.011018149554729462, 0.011019756086170673, 0.011012498289346695, 0.011018883436918259, 0.011017661541700363, 0.01101696491241455, 0.011011648923158646, 0.011018352583050728, 0.01101983804255724, 0.011019024066627026, 0.011015564203262329, 0.011017565615475178], 'lr': [0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 0.00020000001, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 4.0000003e-05, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 8.000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 1.6000001e-06, 3.2000003e-07, 3.2000003e-07, 3.2000003e-07, 3.2000003e-07, 3.2000003e-07, 3.2000003e-07, 3.2000003e-07, 3.2000003e-07]}

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)