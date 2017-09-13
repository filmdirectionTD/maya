from PySide import QtCore, QtGui
import maya.cmds as cmds
import os
import sys


def getTimeRange():
    timerange = []
    timerange.append(int(cmds.playbackOptions(q=True, min=True)) - 5)
    timerange.append(int(cmds.playbackOptions(q=True, max=True)) + 4)
    return timerange


def getShotName():
    mayaSceneName = str(cmds.file(q=True, sn=True)).split('/')[-1]
    shotName = mayaSceneName[:12]

    if (mayaSceneName[3] == '-'):
        return shotName
    else:
        correctedSceneNameList = list(mayaSceneName)
        correctedSceneNameList[3] = '-'
        correctedSceneName = "".join(correctedSceneNameList)
        return ('ERROR: Your animation maya scene name is incorrect\nChange it to ' + correctedSceneName + '\n')


class salutAbcExport(QtGui.QWidget):
    # Scene Data
    baseCachePath = '/projects/SALUT/3D/DATA/CACHE/ANIMATION'
    # List of ORLAN objects
    orlanBaseGeoList = ['geo_cloth_024',
                        'geo_cloth_025',
                        'geo_cloth_027',
                        'geo_cloth_028',
                        'geo_cloth_029',
                        'geo_cloth_030',
                        'geo_cloth_031',
                        'geo_cloth_032',
                        'geo_cloth_033',
                        'geo_cloth_034',
                        'geo_cloth_035',
                        'geo_cloth_045',
                        'geo_cloth_047',
                        'geo_cloth_050',
                        'geo_cloth_051',
                        'geo_ssr_label',
                        'geo_interkosmos_label',
                        'geo_cloth_056',
                        'geo_cloth_061',
                        'geo_metal_05',
                        'geo_metal_0145',
                        'geo_metal_0146',
                        'geo_metal_037',
                        'geo_metal_038',
                        'geo_metal_035',
                        'geo_metal_036',
                        'geo_metal_0140',
                        'geo_metal_0141',
                        'geo_metal_030',
                        'geo_metal_031',
                        'geo_metal_034',
                        'geo_metal_033',
                        'geo_glass_01',
                        'geo_glass_011',
                        'geo_glass_012',
                        'geo_plastic_rubber_01',
                        'geo_plastic_rubber_02',
                        'geo_plastic_rubber_03',
                        'geo_plastic_rubber_04',
                        'geo_plastic_rubber_05',
                        'geo_plastic_rubber_06',
                        'geo_plastic_rubber_07',
                        'geo_plastic_rubber_08',
                        'geo_plastic_rubber_09',
                        'geo_plastic_rubber_010',
                        'geo_plastic_rubber_011',
                        'geo_plastic_rubber_012',
                        'geo_plastic_rubber_013',
                        'geo_plastic_rubber_014',
                        'geo_plastic_rubber_015',
                        'geo_plastic_rubber_016',
                        'geo_plastic_rubber_017',
                        'geo_plastic_rubber_018',
                        'geo_plastic_rubber_019',
                        'geo_plastic_rubber_020',
                        'geo_plastic_rubber_021',
                        'geo_plastic_rubber_022',
                        'geo_plastic_rubber_023',
                        'geo_plastic_rubber_024',
                        'geo_plastic_rubber_025',
                        'geo_plastic_rubber_026',
                        'geo_plastic_rubber_027',
                        'geo_plastic_rubber_028',
                        'geo_plastic_rubber_029',
                        'geo_plastic_rubber_030',
                        'geo_plastic_rubber_031',
                        'geo_plastic_rubber_032',
                        'geo_plastic_rubber_033',
                        'geo_plastic_rubber_034',
                        'geo_plastic_rubber_035',
                        'geo_plastic_rubber_036',
                        'geo_plastic_rubber_037',
                        'geo_plastic_rubber_038',
                        'geo_plastic_rubber_042',
                        'geo_plastic_rubber_043',
                        'geo_plastic_rubber_044',
                        'geo_plastic_rubber_045',
                        'geo_plastic_rubber_046',
                        'geo_plastic_rubber_047',
                        'geo_plastic_rubber_048',
                        'geo_plastic_rubber_049',
                        'geo_plastic_rubber_050',
                        'geo_plastic_rubber_051',
                        'geo_plastic_rubber_052',
                        'geo_plastic_rubber_053',
                        'geo_plastic_rubber_054',
                        'geo_plastic_rubber_055',
                        'geo_plastic_rubber_056',
                        'geo_plastic_rubber_057',
                        'geo_plastic_rubber_058',
                        'geo_plastic_rubber_059',
                        'geo_plastic_rubber_060',
                        'geo_plastic_rubber_061',
                        'geo_cloth_08',
                        'geo_cloth_09',
                        'geo_cloth_011',
                        'geo_cloth_012',
                        'geo_cloth_019',
                        'geo_cloth_021',
                        'geo_cloth_046',
                        'geo_cloth_048',
                        'geo_cloth_07',
                        'geo_cloth_06',
                        'geo_cloth_010',
                        'geo_cloth_01',
                        'geo_cloth_05',
                        'geo_cloth_02',
                        'geo_cloth_03',
                        'geo_cloth_04',
                        'geo_cloth_054',
                        'geo_blazon_label',
                        'geo_cloth_055',
                        'geo_orlan_label',
                        'geo_metal_01',
                        'geo_metal_02',
                        'geo_metal_03',
                        'geo_metal_04',
                        'geo_metal_06',
                        'geo_metal_07',
                        'geo_metal_08',
                        'geo_metal_09',
                        'geo_metal_010',
                        'geo_metal_011',
                        'geo_metal_012',
                        'geo_metal_013',
                        'geo_metal_014',
                        'geo_metal_015',
                        'geo_metal_016',
                        'geo_metal_017',
                        'geo_metal_018',
                        'geo_metal_019',
                        'geo_metal_020',
                        'geo_metal_021',
                        'geo_metal_022',
                        'geo_metal_023',
                        'geo_metal_024',
                        'geo_metal_025',
                        'geo_metal_026',
                        'geo_metal_027',
                        'geo_metal_028',
                        'geo_metal_029',
                        'geo_metal_032',
                        'geo_metal_039',
                        'geo_metal_040',
                        'geo_metal_041',
                        'geo_metal_042',
                        'geo_metal_043',
                        'geo_metal_044',
                        'geo_metal_045',
                        'geo_metal_046',
                        'geo_metal_047',
                        'geo_metal_048',
                        'geo_metal_049',
                        'geo_metal_050',
                        'geo_metal_051',
                        'geo_metal_052',
                        'geo_metal_053',
                        'geo_metal_054',
                        'geo_metal_055',
                        'geo_metal_056',
                        'geo_metal_057',
                        'geo_metal_058',
                        'geo_metal_059',
                        'geo_metal_060',
                        'geo_metal_061',
                        'geo_metal_062',
                        'geo_metal_063',
                        'geo_metal_064',
                        'geo_metal_065',
                        'geo_metal_066',
                        'geo_metal_067',
                        'geo_metal_068',
                        'geo_metal_069',
                        'geo_metal_070',
                        'geo_metal_071',
                        'geo_metal_072',
                        'geo_metal_073',
                        'geo_metal_074',
                        'geo_metal_075',
                        'geo_metal_077',
                        'geo_metal_078',
                        'geo_metal_079',
                        'geo_metal_080',
                        'geo_metal_081',
                        'geo_metal_082',
                        'geo_metal_083',
                        'geo_metal_084',
                        'geo_metal_085',
                        'geo_metal_086',
                        'geo_metal_087',
                        'geo_metal_088',
                        'geo_metal_089',
                        'geo_metal_090',
                        'geo_metal_091',
                        'geo_metal_092',
                        'geo_metal_093',
                        'geo_metal_094',
                        'geo_metal_095',
                        'geo_metal_096',
                        'geo_metal_097',
                        'geo_metal_098',
                        'geo_metal_099',
                        'geo_metal_0100',
                        'geo_metal_0101',
                        'geo_metal_0102',
                        'geo_metal_0103',
                        'geo_metal_0104',
                        'geo_metal_0105',
                        'geo_metal_0106',
                        'geo_metal_0107',
                        'geo_metal_0108',
                        'geo_metal_0109',
                        'geo_metal_0110',
                        'geo_metal_0111',
                        'geo_metal_0112',
                        'geo_metal_0113',
                        'geo_metal_0114',
                        'geo_metal_0115',
                        'geo_metal_0116',
                        'geo_metal_0117',
                        'geo_metal_0118',
                        'geo_metal_0119',
                        'geo_metal_0120',
                        'geo_metal_0121',
                        'geo_metal_0122',
                        'geo_metal_0123',
                        'geo_metal_0124',
                        'geo_metal_0125',
                        'geo_metal_0126',
                        'geo_metal_0127',
                        'geo_metal_0128',
                        'geo_metal_0129',
                        'geo_metal_0130',
                        'geo_metal_0131',
                        'geo_metal_0132',
                        'geo_metal_0133',
                        'geo_metal_0134',
                        'geo_metal_0135',
                        'geo_metal_0136',
                        'geo_metal_0137',
                        'geo_metal_0138',
                        'geo_metal_0139',
                        'geo_metal_0142',
                        'geo_metal_0143',
                        'geo_metal_0144',
                        'geo_metal_0147',
                        'geo_metal_0148',
                        'geo_metal_0149',
                        'geo_metal_0150',
                        'geo_metal_0151',
                        'geo_metal_0152',
                        'geo_metal_0153',
                        'geo_metal_0154',
                        'geo_metal_0155',
                        'geo_metal_0156',
                        'geo_metal_0157',
                        'geo_metal_0158',
                        'geo_metal_0159',
                        'geo_metal_0160',
                        'geo_metal_0166',
                        'geo_metal_0167',
                        'geo_metal_0168',
                        'geo_metal_0169',
                        'geo_metal_0170',
                        'geo_metal_0171',
                        'geo_metal_0172',
                        'geo_metal_0173',
                        'geo_metal_0174',
                        'geo_metal_0175',
                        'geo_metal_0176',
                        'geo_metal_0177',
                        'geo_metal_0178',
                        'geo_metal_0179',
                        'geo_metal_0180',
                        'geo_metal_0181',
                        'geo_metal_0182',
                        'geo_metal_0183',
                        'geo_metal_0184',
                        'geo_metal_0185',
                        'geo_metal_0186',
                        'geo_metal_0187',
                        'geo_metal_0188',
                        'geo_metal_0189',
                        'geo_metal_0190',
                        'geo_metal_0191',
                        'geo_metal_0192',
                        'geo_metal_0193',
                        'geo_metal_0194',
                        'geo_metal_0195',
                        'geo_metal_0196',
                        'geo_metal_0197',
                        'geo_metal_0198',
                        'geo_metal_0199',
                        'geo_metal_0200',
                        'geo_metal_0201',
                        'geo_metal_0202',
                        'geo_metal_0203',
                        'geo_metal_0204',
                        'geo_metal_0205',
                        'geo_metal_0206',
                        'geo_metal_0207',
                        'geo_metal_0208',
                        'geo_metal_0209',
                        'geo_metal_0210',
                        'geo_metal_0211',
                        'geo_metal_0212',
                        'geo_metal_0213',
                        'geo_metal_0214',
                        'geo_metal_0215',
                        'geo_metal_0216',
                        'geo_metal_0217',
                        'geo_metal_0218',
                        'geo_metal_0219',
                        'geo_metal_0220',
                        'geo_metal_0221',
                        'geo_metal_0222',
                        'geo_metal_0223',
                        'geo_metal_0224',
                        'geo_metal_0225',
                        'geo_metal_0226',
                        'geo_metal_0227',
                        'geo_metal_0228',
                        'geo_metal_0229',
                        'geo_metal_0230',
                        'geo_metal_0231',
                        'geo_metal_0232',
                        'geo_metal_0233',
                        'geo_metal_0234',
                        'geo_metal_0235',
                        'geo_metal_0236',
                        'geo_metal_0237',
                        'geo_metal_0238',
                        'geo_metal_0239',
                        'geo_metal_0240',
                        'geo_metal_0241',
                        'geo_metal_0242',
                        'geo_metal_0243',
                        'geo_metal_0244',
                        'geo_metal_0245',
                        'geo_metal_0246',
                        'geo_metal_0247',
                        'geo_metal_0248',
                        'geo_metal_0249',
                        'geo_metal_0250',
                        'geo_metal_0251',
                        'geo_metal_0252',
                        'geo_metal_0253',
                        'geo_metal_0254',
                        'geo_metal_0255',
                        'geo_metal_0256',
                        'geo_metal_0257',
                        'geo_metal_0258',
                        'geo_metal_0259',
                        'geo_metal_0260',
                        'geo_metal_0261',
                        'geo_metal_0262',
                        'geo_metal_0263',
                        'geo_metal_0264',
                        'geo_metal_0265',
                        'geo_metal_0266',
                        'geo_metal_0267',
                        'geo_metal_0268',
                        'geo_metal_0269',
                        'geo_metal_0270',
                        'geo_metal_0271',
                        'geo_metal_0272',
                        'geo_metal_0273',
                        'geo_metal_0274',
                        'geo_metal_0275',
                        'geo_metal_0276',
                        'geo_metal_0277',
                        'geo_metal_0278',
                        'geo_metal_0279',
                        'geo_metal_0280',
                        'geo_metal_0281',
                        'geo_metal_0282',
                        'geo_metal_0283',
                        'geo_metal_0284',
                        'geo_metal_0285',
                        'geo_metal_0286',
                        'geo_metal_0287',
                        'geo_metal_0288',
                        'geo_metal_0289',
                        'geo_metal_0290',
                        'geo_metal_0291',
                        'geo_metal_0292',
                        'geo_metal_0293',
                        'geo_metal_0294',
                        'geo_metal_0295',
                        'geo_metal_0296',
                        'geo_metal_0297',
                        'geo_metal_0298',
                        'geo_metal_0299',
                        'geo_metal_0300',
                        'geo_metal_0301',
                        'geo_metal_0302',
                        'geo_metal_0303',
                        'geo_metal_0304',
                        'geo_metal_0305',
                        'geo_metal_0306',
                        'geo_metal_0307',
                        'geo_metal_0308',
                        'geo_metal_0309',
                        'geo_metal_0310',
                        'geo_metal_0311',
                        'geo_metal_0312',
                        'geo_metal_0313',
                        'geo_metal_0314',
                        'geo_metal_0315',
                        'geo_metal_0316',
                        'geo_metal_0317',
                        'geo_metal_0318',
                        'geo_metal_0319',
                        'geo_metal_0320',
                        'geo_metal_0321',
                        'geo_metal_0322',
                        'geo_metal_0323',
                        'geo_metal_0324',
                        'geo_metal_0325',
                        'geo_metal_0326',
                        'geo_metal_0327',
                        'geo_metal_0328',
                        'geo_metal_0329',
                        'geo_metal_0330',
                        'geo_metal_0331',
                        'geo_metal_0332',
                        'geo_metal_0333',
                        'geo_metal_0334',
                        'geo_metal_0335',
                        'geo_metal_0336',
                        'geo_metal_0337',
                        'geo_metal_0338',
                        'geo_metal_0339',
                        'geo_metal_0340',
                        'geo_metal_0341',
                        'geo_metal_0342',
                        'geo_metal_0343',
                        'geo_metal_0344',
                        'geo_metal_0345',
                        'geo_metal_0346',
                        'geo_metal_0347',
                        'geo_metal_0348',
                        'geo_metal_0349',
                        'geo_metal_0350',
                        'geo_metal_0351',
                        'geo_metal_0352',
                        'geo_metal_0353',
                        'geo_metal_0354',
                        'geo_metal_0355',
                        'geo_metal_0356',
                        'geo_metal_0357',
                        'geo_metal_0358',
                        'geo_metal_0359',
                        'geo_metal_0360',
                        'geo_metal_0361',
                        'geo_metal_0362',
                        'geo_metal_0363',
                        'geo_metal_0364',
                        'geo_metal_0365',
                        'geo_metal_0366',
                        'geo_metal_0367',
                        'geo_metal_0368',
                        'geo_metal_0369',
                        'geo_metal_0370',
                        'geo_metal_0371',
                        'geo_metal_0372',
                        'geo_metal_0373',
                        'geo_metal_0374',
                        'geo_metal_0375',
                        'geo_metal_0376',
                        'geo_metal_0377',
                        'geo_metal_0378',
                        'geo_metal_0379',
                        'geo_metal_0380',
                        'geo_metal_0381',
                        'geo_metal_0382',
                        'geo_metal_0383',
                        'geo_metal_0384',
                        'geo_metal_0385',
                        'geo_metal_0386',
                        'geo_metal_0387',
                        'geo_metal_0388',
                        'geo_metal_0389',
                        'geo_metal_0390',
                        'geo_metal_0391',
                        'geo_metal_0392',
                        'geo_metal_0393',
                        'geo_metal_0394',
                        'geo_metal_0395',
                        'geo_metal_0396',
                        'geo_metal_0397',
                        'geo_metal_0398',
                        'geo_metal_0399',
                        'geo_metal_0400',
                        'geo_metal_0401',
                        'geo_metal_0402',
                        'geo_metal_0464',
                        'geo_metal_0465',
                        'geo_metal_0466',
                        'geo_metal_0467',
                        'geo_metal_0468',
                        'geo_metal_0469',
                        'geo_metal_076',
                        'geo_metal_0470',
                        'geo_metal_0162',
                        'geo_metal_0163',
                        'geo_metal_0164',
                        'geo_metal_0165',
                        'geo_metal_0161',
                        'geo_glass_03',
                        'geo_glass_04',
                        'geo_glass_05',
                        'geo_glass_06',
                        'geo_glass_07',
                        'geo_glass_08',
                        'geo_glass_09',
                        'geo_glass_010',
                        'geo_glass_013',
                        'geo_glass_014',
                        'geo_glass_015',
                        'geo_glass_016',
                        'geo_glass_017',
                        'geo_glass_018',
                        'geo_glass_019',
                        'geo_glass_020',
                        'geo_glass_021',
                        'geo_glass_02',
                        'geo_plastic_rubber_040',
                        'geo_plastic_rubber_039',
                        'geo_plastic_rubber_041',
                        'geo_cloth_044',
                        'geo_cloth_038',
                        'geo_cloth_036',
                        'geo_cloth_041',
                        'geo_cloth_042',
                        'geo_metal_0447',
                        'geo_metal_0448',
                        'geo_metal_0460',
                        'geo_metal_0461',
                        'geo_metal_0463',
                        'geo_metal_0449',
                        'geo_metal_0450',
                        'geo_metal_0451',
                        'geo_metal_0452',
                        'geo_metal_0453',
                        'geo_metal_0454',
                        'geo_metal_0455',
                        'geo_metal_0456',
                        'geo_metal_0457',
                        'geo_metal_0458',
                        'geo_metal_0459',
                        'geo_metal_0462',
                        'geo_metal_0411',
                        'geo_metal_0412',
                        'geo_metal_0413',
                        'geo_metal_0414',
                        'geo_metal_0415',
                        'geo_metal_0416',
                        'geo_metal_0435',
                        'geo_metal_0436',
                        'geo_metal_0437',
                        'geo_metal_0438',
                        'geo_metal_0439',
                        'geo_metal_0440',
                        'geo_metal_0441',
                        'geo_metal_0442',
                        'geo_metal_0443',
                        'geo_metal_0444',
                        'geo_metal_0445',
                        'geo_metal_0446',
                        'geo_cloth_043',
                        'geo_metal_0427',
                        'geo_metal_0430',
                        'geo_metal_0433',
                        'geo_metal_0417',
                        'geo_metal_0418',
                        'geo_metal_0419',
                        'geo_metal_0420',
                        'geo_metal_0421',
                        'geo_metal_0422',
                        'geo_metal_0423',
                        'geo_metal_0424',
                        'geo_metal_0425',
                        'geo_metal_0426',
                        'geo_metal_0428',
                        'geo_metal_0429',
                        'geo_metal_0431',
                        'geo_metal_0432',
                        'geo_metal_0434',
                        'geo_cloth_039',
                        'geo_cloth_040',
                        'orlan_modl_geo_metal_0410',
                        'orlan_modl_geo_metal_0408',
                        'orlan_modl_geo_metal_0409',
                        'orlan_modl_geo_metal_0407',
                        'orlan_modl_geo_metal_0405',
                        'orlan_modl_geo_metal_0406',
                        'orlan_modl_geo_metal_0404',
                        'orlan_modl_geo_metal_0403',
                        'orlan_modl_geo_cloth_037']

    anchorBaseList = ['geo_metal_311',
                        'geo_metal_310',
                        'geo_metal_102',
                        'geo_metal_101',
                        'geo_metal_100',
                        'geo_metal_103',
                        'geo_metal_88',
                        'geo_metal_87',
                        'geo_metal_89',
                        'geo_metal_90',
                        'geo_metal_95',
                        'geo_metal_312',
                        'geo_metal_99',
                        'geo_metal_96',
                        'geo_metal_98',
                        'geo_metal_97',
                        'geo_metal_117',
                        'geo_metal_129',
                        'geo_metal_116',
                        'geo_metal_131',
                        'geo_metal_130',
                        'geo_metal_132',
                        'geo_metal_313',
                        'geo_metal_128',
                        'geo_metal_125',
                        'geo_metal_127',
                        'geo_metal_126',
                        'geo_metal_124',
                        'geo_metal_67',
                        'geo_metal_118',
                        'geo_metal_119',
                        'geo_metal_314',
                        'geo_metal_123',
                        'geo_metal_122',
                        'geo_metal_93',
                        'geo_metal_94',
                        'geo_metal_91',
                        'geo_metal_120',
                        'polySurface4',
                        'polySurface2',
                        'polySurface3',
                        'geo_metal_104',
                        'geo_metal_83',
                        'geo_metal_112',
                        'polySurface1',
                        'geo_metal_133',
                        'geo_rubber_1',
                        'geo_plastic_2',
                        'geo_plastic_1',
                        'geo_rubber_2',
                        'geo_plastic_9',
                        'geo_plastic_11',
                        'geo_plastic_10',
                        'geo_plastic_8',
                        'geo_plastic_7',
                        'geo_plastic_6',
                        'geo_plastic_5',
                        'geo_plastic_4',
                        'geo_plastic_3',
                        'geo_metal_10',
                        'geo_metal_11',
                        'geo_metal_12',
                        'geo_metal_13',
                        'geo_metal_14',
                        'geo_metal_15',
                        'geo_metal_16',
                        'geo_metal_17',
                        'geo_metal_18',
                        'geo_metal_19',
                        'geo_metal_20',
                        'geo_metal_22',
                        'geo_metal_23',
                        'geo_metal_24',
                        'geo_metal_25',
                        'geo_metal_26',
                        'geo_metal_27',
                        'geo_metal_28',
                        'geo_metal_29',
                        'geo_metal_30',
                        'geo_metal_31',
                        'geo_metal_32',
                        'geo_metal_33',
                        'geo_metal_34',
                        'geo_metal_35',
                        'geo_metal_36',
                        'geo_metal_37',
                        'geo_metal_38',
                        'geo_metal_39',
                        'geo_metal_40',
                        'geo_metal_41',
                        'geo_metal_42',
                        'geo_metal_43',
                        'geo_metal_44',
                        'geo_metal_45',
                        'geo_metal_46',
                        'geo_metal_47',
                        'geo_metal_48',
                        'geo_metal_49',
                        'geo_metal_50',
                        'geo_metal_51',
                        'geo_metal_52',
                        'geo_metal_53',
                        'geo_metal_54',
                        'geo_metal_55',
                        'geo_metal_56',
                        'geo_metal_57',
                        'geo_metal_58',
                        'geo_metal_59',
                        'geo_metal_60',
                        'geo_metal_61',
                        'geo_metal_62',
                        'geo_metal_134',
                        'geo_metal_135',
                        'geo_metal_136',
                        'geo_metal_137',
                        'geo_metal_138',
                        'geo_metal_139',
                        'geo_metal_140',
                        'geo_metal_141',
                        'geo_metal_142',
                        'geo_metal_143',
                        'geo_metal_144',
                        'geo_metal_145',
                        'geo_metal_146',
                        'geo_metal_147',
                        'geo_metal_148',
                        'geo_metal_149',
                        'geo_metal_150',
                        'geo_metal_151',
                        'geo_metal_152',
                        'geo_metal_153',
                        'geo_metal_154',
                        'geo_metal_155',
                        'geo_metal_156',
                        'geo_metal_157',
                        'geo_metal_158',
                        'geo_metal_159',
                        'geo_metal_160',
                        'geo_metal_1',
                        'geo_metal_2',
                        'geo_metal_3',
                        'geo_metal_4',
                        'geo_metal_5',
                        'geo_metal_6',
                        'geo_metal_7',
                        'geo_metal_8',
                        'geo_metal_9',
                        'geo_metal_162',
                        'geo_metal_318',
                        'geo_metal_163',
                        'geo_metal_319',
                        'geo_metal_305',
                        'geo_metal_307',
                        'geo_metal_306',
                        'geo_metal_76',
                        'geo_metal_77',
                        'geo_metal_78',
                        'geo_metal_79',
                        'geo_metal_82',
                        'geo_metal_84',
                        'geo_metal_85',
                        'geo_metal_86',
                        'geo_metal_64',
                        'geo_metal_105',
                        'geo_metal_106',
                        'geo_metal_107',
                        'geo_metal_108',
                        'geo_metal_109',
                        'geo_metal_113',
                        'geo_metal_114',
                        'geo_metal_115',
                        'geo_metal_110',
                        'geo_metal_111',
                        'geo_metal_315',
                        'geo_metal_316',
                        'geo_metal_317',
                        'geo_metal_309',
                        'geo_metal_308',
                        'geo_metal_65',
                        'geo_metal_80',
                        'geo_metal_81',
                        'geo_metal_164',
                        'geo_metal_165',
                        'geo_metal_68',
                        'geo_metal_69',
                        'geo_metal_70',
                        'geo_metal_71',
                        'geo_metal_72',
                        'geo_metal_73',
                        'geo_metal_74',
                        'geo_metal_75',
                        'geo_metal_161',
                        'geo_metal_66',
                        'geo_metal_63',
                        'geo_metal_21']

    cameraBaseList =['geo_metall_1',
                        'geo_metall_2',
                        'geo_metall_3',
                        'geo_metall_4',
                        'geo_metall_5',
                        'geo_metall_6',
                        'geo_metall_7',
                        'geo_metall_8',
                        'geo_metall_9',
                        'geo_metall_10',
                        'geo_metall_11',
                        'geo_metall_12',
                        'geo_metall_13',
                        'geo_metall_14',
                        'geo_metall_15',
                        'geo_metall_16',
                        'geo_metall_17',
                        'geo_metall_18',
                        'geo_metall_19',
                        'geo_metall_20',
                        'geo_metall_21',
                        'geo_metall_22',
                        'geo_metall_23',
                        'geo_metall_24',
                        'geo_metall_25',
                        'geo_metall_26',
                        'geo_metall_27',
                        'geo_metall_28',
                        'geo_metall_29',
                        'geo_metall_30',
                        'geo_metall_31',
                        'geo_metall_32',
                        'geo_metall_33',
                        'geo_metall_34',
                        'geo_metall_35',
                        'geo_metall_36',
                        'geo_metall_37',
                        'geo_metall_38',
                        'geo_metall_39',
                        'geo_metall_40',
                        'geo_metall_41',
                        'geo_metall_42',
                        'geo_metall_43',
                        'geo_metall_44',
                        'geo_metall_45',
                        'geo_metall_46',
                        'geo_metall_47',
                        'geo_metall_48',
                        'geo_metall_49',
                        'geo_metall_50',
                        'geo_metall_51',
                        'geo_metall_52',
                        'geo_metall_53',
                        'geo_metall_54',
                        'geo_metall_55',
                        'geo_metall_56',
                        'geo_metall_57',
                        'geo_metall_58',
                        'geo_metall_59',
                        'geo_metall_60',
                        'geo_metall_61',
                        'geo_metall_62',
                        'geo_metall_63',
                        'geo_metall_64',
                        'geo_metall_65',
                        'geo_metall_66',
                        'geo_metall_67',
                        'geo_metall_68',
                        'geo_metall_69',
                        'geo_metall_70',
                        'geo_metall_71',
                        'geo_metall_black1',
                        'geo_metall_black2',
                        'geo_metall_black3',
                        'geo_metall_black4',
                        'geo_metall_black5',
                        'geo_metall_black6',
                        'geo_metall_black7',
                        'geo_metall_black8',
                        'geo_metall_black9',
                        'geo_metall_black10',
                        'geo_metall_black11',
                        'geo_metall_black12',
                        'geo_metall_black13',
                        'geo_metall_black14',
                        'geo_metall_black15',
                        'geo_glass_1',
                        'geo_glass_2',
                        'geo_glass_3',
                        'geo_glass_4',
                        'geo_glass_5',
                        'geo_glass_6',
                        'geo_plastic_black_1',
                        'geo_plastic_black_2',
                        'geo_plastic_black_3',
                        'geo_plastic_black_4',
                        'geo_plastic_black_5',
                        'geo_plastic_black_6',
                        'geo_plastic_black_7',
                        'geo_plastic_black_8',
                        'geo_plastic_black_9',
                        'geo_plastic_black_10',
                        'geo_plastic_black_11',
                        'geo_plastic_black_12',
                        'geo_plastic_black_13',
                        'geo_plastic_black_14',
                        'geo_plastic_black_15',
                        'geo_plastic_black_16',
                        'geo_plastic_black_17',
                        'geo_plastic_black_18',
                        'geo_plastic_black_19',
                        'geo_plastic_black_20',
                        'geo_plastic_black_21',
                        'geo_labels_red_1',
                        'geo_labels_red_2',
                        'geo_labels_red_3',
                        'geo_labels_red_4',
                        'geo_labels_red_5',
                        'geo_labels_red_6',
                        'geo_labels_red_7',
                        'geo_labels_red_8',
                        'geo_labels_red_9',
                        'geo_labels_red_10',
                        'geo_labels_red_11',
                        'geo_labels_red_12',
                        'geo_labels_red_13',
                        'geo_labels_red_14',
                        'geo_labels_red_15',
                        'geo_labels_red_16',
                        'geo_labels_red_17',
                        'geo_labels_red_18',
                        'geo_labels_red_19',
                        'geo_labels_red_20',
                        'geo_labels_red_21',
                        'geo_labels_red_22',
                        'geo_labels_red_23',
                        'geo_labels_red_24',
                        'geo_labels_red_25',
                        'geo_labels_red_26',
                        'geo_labels_red_27',
                        'geo_labels_red_28',
                        'geo_labels_red_29',
                        'geo_labels_red_30',
                        'geo_labels_red_31',
                        'geo_labels_red_32',
                        'geo_labels_red_33',
                        'geo_labels_red_34',
                        'geo_labels_red_35',
                        'geo_labels_red_36',
                        'geo_labels_red_37',
                        'geo_labels_red_38',
                        'geo_labels_red_39',
                        'geo_labels_red_40',
                        'geo_labels_red_41',
                        'geo_labels_red_42',
                        'geo_labels_red_43',
                        'geo_labels_red_44',
                        'geo_labels_red_45',
                        'geo_labels_red_46',
                        'geo_labels_red_47',
                        'geo_labels_red_48',
                        'geo_labels_red_49',
                        'geo_labels_red_50',
                        'geo_labels_red_51',
                        'geo_labels_red_52',
                        'geo_labels_red_53',
                        'geo_labels_red_54',
                        'geo_labels_red_55',
                        'geo_labels_red_56',
                        'geo_labels_red_57',
                        'geo_labels_red_58',
                        'geo_labels_red_59',
                        'geo_labels_red_60',
                        'geo_labels_red_61',
                        'geo_labels_red_62',
                        'geo_labels_red_63',
                        'geo_labels_red_64',
                        'geo_labels_red_65',
                        'geo_labels_red_66',
                        'geo_labels_red_67',
                        'geo_labels_red_68',
                        'geo_labels_red_69',
                        'geo_labels_red_70',
                        'geo_labels_red_71',
                        'geo_labels_red_72',
                        'geo_labels_red_73',
                        'geo_labels_red_74',
                        'geo_labels_red_75',
                        'geo_labels_red_76',
                        'geo_labels_red_77',
                        'geo_labels_red_78',
                        'geo_labels_red_79',
                        'geo_labels_red_80',
                        'geo_labels_red_81',
                        'geo_labels_red_82',
                        'geo_labels_red_83',
                        'geo_labels_red_84',
                        'geo_labels_red_85',
                        'geo_labels_red_86',
                        'geo_labels_red_87',
                        'geo_labels_red_88',
                        'geo_labels_red_89',
                        'geo_labels_red_90',
                        'geo_labels_red_91',
                        'geo_labels_red_92',
                        'geo_labels_red_93',
                        'geo_labels_red_94',
                        'geo_labels_red_95',
                        'geo_labels_red_96',
                        'geo_labels_red_97',
                        'geo_labels_red_98',
                        'geo_labels_red_99',
                        'geo_labels_red_100',
                        'geo_labels_red_101',
                        'geo_labels_red_102',
                        'geo_labels_red_103',
                        'geo_labels_red_104',
                        'geo_labels_red_105',
                        'geo_labels_red_106',
                        'geo_labels_red_107',
                        'geo_labels_red_108',
                        'geo_labels_red_109',
                        'geo_labels_red_110',
                        'geo_labels_red_111',
                        'geo_labels_red_112',
                        'geo_labels_red_113',
                        'geo_labels_red_114',
                        'geo_labels_red_115',
                        'geo_labels_red_116',
                        'geo_labels_red_117',
                        'geo_labels_red_118',
                        'geo_labels_red_119',
                        'geo_labels_red_120',
                        'geo_labels_red_121',
                        'geo_labels_white_1',
                        'geo_labels_white_2',
                        'geo_labels_white_3',
                        'geo_labels_white_4',
                        'geo_labels_white_5',
                        'geo_labels_white_6',
                        'geo_labels_white_7',
                        'geo_labels_white_8',
                        'geo_labels_white_9',
                        'geo_labels_white_10',
                        'geo_labels_white_11',
                        'geo_labels_white_12',
                        'geo_labels_white_13',
                        'geo_labels_white_14',
                        'geo_labels_white_15',
                        'geo_labels_white_16',
                        'geo_labels_white_17',
                        'geo_labels_white_18',
                        'geo_labels_white_19',
                        'geo_labels_white_20',
                        'geo_labels_white_21',
                        'geo_labels_white_22',
                        'geo_labels_white_23',
                        'geo_labels_white_24',
                        'geo_labels_white_25',
                        'geo_labels_white_26',
                        'geo_labels_white_27',
                        'geo_labels_white_28',
                        'geo_labels_white_29',
                        'geo_labels_white_30',
                        'geo_labels_white_31',
                        'geo_labels_white_32',
                        'geo_labels_white_33',
                        'geo_labels_white_34',
                        'geo_labels_white_35',
                        'geo_labels_white_36',
                        'geo_labels_white_37',
                        'geo_labels_white_38',
                        'geo_labels_white_39',
                        'geo_labels_white_40',
                        'geo_labels_white_41',
                        'geo_labels_white_42',
                        'geo_labels_white_43',
                        'geo_labels_white_44',
                        'geo_labels_white_45',
                        'geo_labels_white_46',
                        'geo_labels_white_47',
                        'geo_labels_white_48',
                        'geo_labels_white_49',
                        'geo_labels_white_50',
                        'geo_labels_white_51',
                        'geo_labels_white_52',
                        'geo_labels_white_53',
                        'geo_labels_white_54',
                        'geo_labels_white_55',
                        'geo_labels_white_56',
                        'geo_labels_white_57',
                        'geo_labels_white_58',
                        'geo_labels_white_59',
                        'geo_labels_white_60',
                        'geo_labels_white_61',
                        'geo_labels_white_62',
                        'geo_labels_white_63',
                        'geo_labels_white_64',
                        'geo_labels_white_65',
                        'geo_labels_white_66',
                        'geo_labels_white_67',
                        'geo_labels_white_68',
                        'geo_labels_white_69',
                        'geo_labels_white_70',
                        'geo_labels_white_71',
                        'geo_labels_white_72',
                        'geo_labels_white_73',
                        'geo_labels_white_74',
                        'geo_labels_white_75',
                        'geo_labels_white_76',
                        'geo_labels_white_77',
                        'geo_labels_white_78',
                        'geo_labels_white_79',
                        'geo_labels_white_80',
                        'geo_labels_white_81',
                        'geo_labels_white_82',
                        'geo_labels_white_83',
                        'geo_labels_white_84',
                        'geo_labels_white_85',
                        'geo_labels_white_86',
                        'geo_labels_white_87',
                        'geo_labels_white_88',
                        'geo_labels_white_89',
                        'geo_labels_white_90',
                        'geo_labels_white_91',
                        'geo_labels_white_92',
                        'geo_labels_white_93',
                        'geo_labels_white_94',
                        'geo_labels_white_95',
                        'geo_labels_white_96',
                        'geo_labels_white_97',
                        'geo_labels_white_98',
                        'geo_labels_white_99',
                        'geo_labels_white_100',
                        'geo_labels_white_101',
                        'geo_labels_white_102',
                        'geo_labels_white_103',
                        'geo_labels_white_104',
                        'geo_labels_white_105',
                        'geo_labels_white_106',
                        'geo_labels_white_107',
                        'geo_labels_white_108',
                        'geo_labels_white_109',
                        'geo_labels_white_110',
                        'geo_labels_white_111',
                        'geo_labels_white_112',
                        'geo_labels_white_113',
                        'geo_labels_white_114',
                        'geo_labels_white_115',
                        'geo_labels_white_116',
                        'geo_labels_white_117',
                        'geo_labels_white_118',
                        'geo_labels_white_119',
                        'geo_labels_white_120',
                        'geo_labels_white_121',
                        'geo_labels_white_122',
                        'geo_labels_white_123',
                        'geo_labels_white_124',
                        'geo_labels_white_125',
                        'geo_labels_white_126',
                        'geo_labels_white_127',
                        'geo_labels_white_128',
                        'geo_labels_white_129',
                        'geo_labels_white_130',
                        'geo_labels_white_131',
                        'geo_labels_white_132',
                        'geo_labels_white_133',
                        'geo_labels_white_134',
                        'geo_labels_white_135',
                        'geo_labels_white_136',
                        'geo_labels_white_137',
                        'geo_labels_white_138',
                        'geo_labels_white_139',
                        'geo_labels_white_140',
                        'geo_labels_white_141',
                        'geo_labels_white_142',
                        'geo_labels_white_143',
                        'geo_labels_white_144',
                        'geo_labels_white_145',
                        'geo_labels_white_146',
                        'geo_labels_white_147',
                        'geo_labels_white_148',
                        'geo_labels_white_149',
                        'geo_labels_white_150',
                        'geo_labels_white_151',
                        'geo_labels_white_152',
                        'geo_labels_white_153',
                        'geo_labels_white_154',
                        'geo_labels_white_155',
                        'geo_labels_white_156',
                        'geo_labels_white_157',
                        'geo_labels_white_158',
                        'geo_labels_white_159',
                        'geo_labels_white_160',
                        'geo_labels_white_161',
                        'geo_labels_white_162',
                        'geo_labels_white_163',
                        'geo_labels_white_164',
                        'geo_labels_white_165',
                        'geo_labels_white_166',
                        'geo_labels_white_167',
                        'geo_labels_white_168',
                        'geo_labels_white_169',
                        'geo_labels_white_170',
                        'geo_labels_white_171',
                        'geo_labels_white_172',
                        'geo_labels_white_173',
                        'geo_labels_white_174',
                        'geo_labels_white_175',
                        'geo_labels_white_176',
                        'geo_labels_white_177',
                        'geo_labels_white_178',
                        'geo_labels_white_179',
                        'geo_labels_white_180',
                        'geo_labels_white_181',
                        'geo_labels_white_182',
                        'geo_labels_white_183',
                        'geo_labels_white_184',
                        'geo_labels_white_185',
                        'geo_labels_white_186',
                        'geo_labels_white_187',
                        'geo_labels_white_188',
                        'geo_labels_white_189',
                        'geo_labels_white_190',
                        'geo_labels_white_191',
                        'geo_labels_white_192',
                        'geo_labels_white_193',
                        'geo_labels_white_194',
                        'geo_labels_white_195',
                        'geo_labels_white_196',
                        'geo_labels_white_197',
                        'geo_labels_white_198',
                        'geo_labels_white_199',
                        'geo_labels_white_200',
                        'geo_labels_white_201',
                        'geo_labels_white_202',
                        'geo_labels_white_203',
                        'geo_labels_white_204',
                        'geo_labels_white_205',
                        'geo_labels_white_206',
                        'geo_labels_white_207',
                        'geo_labels_white_208',
                        'geo_labels_white_209',
                        'geo_labels_white_210',
                        'geo_labels_white_211',
                        'geo_labels_white_212',
                        'geo_labels_white_213',
                        'geo_labels_white_214',
                        'geo_labels_white_215',
                        'geo_labels_white_216',
                        'geo_labels_white_217',
                        'geo_labels_white_218',
                        'geo_labels_white_219',
                        'geo_labels_white_220',
                        'geo_labels_white_221',
                        'geo_labels_white_222',
                        'geo_labels_white_223',
                        'geo_labels_white_224',
                        'geo_labels_white_225',
                        'geo_labels_white_226',
                        'geo_labels_white_227',
                        'geo_labels_white_228',
                        'geo_labels_white_229',
                        'geo_labels_white_230',
                        'geo_labels_white_231',
                        'geo_labels_white_232',
                        'geo_labels_white_233',
                        'geo_labels_white_234',
                        'geo_labels_white_235',
                        'geo_labels_white_236',
                        'geo_labels_white_237',
                        'geo_labels_white_238',
                        'geo_labels_white_239',
                        'geo_labels_white_240',
                        'geo_labels_white_241',
                        'geo_labels_white_242',
                        'geo_labels_white_243',
                        'geo_labels_white_244',
                        'geo_labels_white_245',
                        'geo_labels_white_246',
                        'geo_labels_white_247',
                        'geo_labels_white_248',
                        'geo_labels_white_249',
                        'geo_labels_white_250',
                        'geo_labels_white_251',
                        'geo_labels_white_252',
                        'geo_labels_white_253',
                        'geo_labels_white_254',
                        'geo_labels_white_255',
                        'geo_labels_white_256',
                        'geo_labels_white_257',
                        'geo_labels_white_258',
                        'geo_labels_white_259',
                        'geo_labels_white_260',
                        'geo_labels_white_261',
                        'geo_labels_white_262',
                        'geo_labels_white_263',
                        'geo_labels_white_264',
                        'geo_labels_white_265',
                        'geo_labels_white_266',
                        'geo_labels_white_267',
                        'geo_labels_white_268',
                        'geo_labels_white_269',
                        'geo_labels_white_270',
                        'geo_labels_white_271',
                        'geo_labels_white_272',
                        'geo_labels_white_273',
                        'geo_labels_white_274',
                        'geo_labels_white_275',
                        'geo_labels_white_276',
                        'geo_labels_white_277',
                        'geo_labels_white_278',
                        'geo_labels_white_279',
                        'geo_labels_white_280',
                        'geo_labels_white_281',
                        'geo_labels_white_282',
                        'geo_labels_white_283',
                        'geo_labels_white_284',
                        'geo_labels_white_285',
                        'geo_labels_white_286',
                        'geo_labels_white_287',
                        'geo_labels_white_288',
                        'geo_labels_white_289',
                        'geo_labels_white_290',
                        'geo_labels_white_291',
                        'geo_labels_white_292',
                        'geo_labels_white_293',
                        'geo_labels_white_294',
                        'geo_labels_white_295',
                        'geo_labels_white_296',
                        'geo_labels_white_297',
                        'geo_labels_white_298',
                        'geo_labels_white_299',
                        'geo_labels_white_300',
                        'geo_labels_white_301',
                        'geo_labels_white_302',
                        'geo_labels_white_303',
                        'geo_labels_white_304',
                        'geo_labels_white_305',
                        'geo_labels_white_306',
                        'geo_labels_white_307',
                        'geo_labels_white_308',
                        'geo_labels_white_309',
                        'geo_labels_white_310',
                        'geo_labels_white_311',
                        'geo_labels_white_312',
                        'geo_labels_white_313',
                        'geo_labels_white_314',
                        'geo_labels_white_315',
                        'geo_labels_white_316',
                        'geo_labels_white_317',
                        'geo_labels_white_318',
                        'geo_labels_white_319',
                        'geo_labels_white_320',
                        'geo_labels_white_321',
                        'geo_labels_white_322',
                        'geo_labels_white_323',
                        'geo_labels_white_324',
                        'geo_labels_white_325',
                        'geo_labels_white_326',
                        'geo_labels_white_327',
                        'geo_labels_white_328',
                        'geo_labels_white_329',
                        'geo_labels_white_330',
                        'geo_labels_white_331',
                        'geo_labels_white_332',
                        'geo_labels_white_333',
                        'geo_labels_white_334',
                        'geo_labels_white_335',
                        'geo_labels_white_336',
                        'geo_labels_white_337',
                        'geo_labels_white_338',
                        'geo_labels_white_339',
                        'geo_labels_white_340',
                        'geo_labels_white_341',
                        'geo_labels_white_342',
                        'geo_labels_white_343',
                        'geo_labels_white_344',
                        'geo_labels_white_345',
                        'geo_labels_white_346',
                        'geo_labels_white_347',
                        'geo_labels_white_348',
                        'geo_labels_white_349',
                        'geo_labels_white_350',
                        'geo_labels_white_351',
                        'geo_labels_white_352',
                        'geo_labels_white_353',
                        'geo_labels_white_354']

    hammerBaseList = ['geo_hammer']

    hatchBaseList = ['geo_metal1',
                     'geo_metal2',
                     'geo_metal3',
                     'geo_metal4',
                     'geo_metal5',
                     'geo_metal6',
                     'geo_metal7',
                     'geo_metal8',
                     'geo_metal9',
                     'geo_metal10',
                     'geo_metal11',
                     'geo_metal12',
                     'geo_metal13',
                     'geo_metal14',
                     'geo_metal15',
                     'geo_metal16',
                     'geo_metal17',
                     'geo_metal18',
                     'geo_metal19',
                     'geo_metal20',
                     'geo_metal21',
                     'geo_metal22',
                     'geo_metal23',
                     'geo_metal24',
                     'geo_metal25',
                     'geo_metal26',
                     'geo_metal27',
                     'geo_metal28',
                     'geo_metal29',
                     'geo_metal30',
                     'geo_metal31',
                     'geo_metal32',
                     'geo_metal33',
                     'geo_metal34',
                     'geo_metal35',
                     'geo_metal36',
                     'geo_metal37',
                     'geo_metal38',
                     'geo_metal39',
                     'geo_metal40',
                     'geo_metal41',
                     'geo_metal42',
                     'geo_metal43',
                     'geo_metal44',
                     'geo_metal45',
                     'geo_metal46',
                     'geo_metal47',
                     'geo_metal48',
                     'geo_metal49',
                     'geo_metal50',
                     'geo_metal51',
                     'geo_metal52',
                     'geo_metal53',
                     'geo_metal54',
                     'geo_metal55',
                     'geo_metal56',
                     'geo_metal57',
                     'geo_metal58',
                     'geo_metal59',
                     'geo_metal60',
                     'geo_metal61',
                     'geo_metal62',
                     'geo_metal63',
                     'geo_metal64',
                     'geo_metal65',
                     'geo_metal66',
                     'geo_metal67',
                     'geo_metal68',
                     'geo_metal69',
                     'geo_metal70',
                     'geo_metal71',
                     'geo_metal72',
                     'geo_metal73',
                     'geo_metal74',
                     'geo_metal75',
                     'geo_metal76',
                     'geo_metal77',
                     'geo_metal78',
                     'geo_metal79',
                     'geo_metal80',
                     'geo_metal81',
                     'geo_metal82',
                     'geo_metal83',
                     'geo_metal84',
                     'geo_metal85',
                     'pasted__polySurface16',
                     'pasted__pasted__geo_metal1016',
                     'pasted__pCylinder40',
                     'pasted__pasted__geo_metal1015',
                     'pasted__pasted__geo_metal1017',
                     'pasted__polySurface47',
                     'pasted__pCylinder28',
                     'pasted__pasted__geo_metal1018',
                     'pasted__polySurface53',
                     'pasted__polySurface52',
                     'pasted__polySurface33',
                     'pasted__polySurface34',
                     'geo_metal_329',
                     'geo_metal_330',
                     'geo_metal_331',
                     'geo_metal_332',
                     'geo_metal_333',
                     'geo_metal_334',
                     'geo_metal_335',
                     'geo_metal_336',
                     'geo_metal_337',
                     'geo_metal_338',
                     'geo_metal_342',
                     'geo_metal_343',
                     'geo_metal_344',
                     'geo_metal_316',
                     'geo_metal_315',
                     'geo_metal_340',
                     'geo_metal_339',
                     'geo_metal_328',
                     'geo_metal_326',
                     'geo_metal_305',
                     'geo_metal_306',
                     'geo_metal_307',
                     'geo_metal_308',
                     'geo_metal_309',
                     'geo_metal_310',
                     'geo_metal_311',
                     'geo_metal_312',
                     'geo_metal_313',
                     'geo_metal_314',
                     'geo_metal_317',
                     'geo_metal_318',
                     'geo_metal_319',
                     'geo_metal_320',
                     'geo_metal_321',
                     'geo_metal_322',
                     'geo_metal_327',
                     'geo_metal_324',
                     'geo_metal_345',
                     'geo_metal_323',
                     'geo_metal_346',
                     'geo_metal_325',
                     'geo_metal_341',
                     'geo_metal92',
                     'geo_metal93',
                     'geo_metal94',
                     'geo_metal95',
                     'geo_metal96',
                     'geo_metal97',
                     'geo_metal98',
                     'geo_metal99',
                     'geo_metal100',
                     'geo_metal101',
                     'geo_metal102',
                     'geo_metal103',
                     'geo_metal104',
                     'geo_metal105',
                     'geo_metal106',
                     'geo_metal107',
                     'geo_metal108',
                     'geo_metal109',
                     'geo_metal110',
                     'geo_metal111',
                     'geo_metal112',
                     'geo_metal113',
                     'geo_metal114',
                     'geo_metal115',
                     'geo_metal116',
                     'geo_metal117',
                     'geo_metal118',
                     'geo_metal119',
                     'geo_metal120',
                     'geo_metal121',
                     'geo_metal122',
                     'geo_metal123',
                     'geo_metal124',
                     'geo_metal125',
                     'geo_metal126',
                     'geo_metal127',
                     'geo_metal128',
                     'geo_metal129',
                     'geo_metal130',
                     'geo_metal131',
                     'geo_metal132',
                     'geo_metal133',
                     'geo_metal134',
                     'geo_metal135',
                     'geo_metal136',
                     'geo_metal137',
                     'geo_metal138',
                     'geo_metal139',
                     'geo_metal140',
                     'geo_metal141',
                     'geo_metal142',
                     'geo_metal143',
                     'geo_metal144',
                     'geo_metal145',
                     'geo_metal146',
                     'geo_metal147',
                     'geo_metal148',
                     'geo_metal149',
                     'geo_metal150',
                     'geo_metal151',
                     'geo_metal152',
                     'geo_metal153',
                     'geo_metal154',
                     'geo_metal155',
                     'geo_metal156',
                     'geo_metal157',
                     'geo_metal158',
                     'geo_metal159',
                     'geo_metal160',
                     'geo_metal161',
                     'geo_metal162',
                     'geo_metal163',
                     'geo_metal164',
                     'geo_metal165',
                     'geo_metal166',
                     'geo_metal167',
                     'geo_metal168',
                     'geo_metal169',
                     'geo_metal170',
                     'geo_metal171',
                     'geo_metal172',
                     'geo_metal173',
                     'geo_metal174',
                     'geo_metal175',
                     'geo_metal176',
                     'geo_metal177',
                     'geo_metal178',
                     'geo_metal179',
                     'geo_metal180',
                     'geo_metal181',
                     'geo_metal182',
                     'geo_metal183',
                     'geo_metal184',
                     'geo_metal185',
                     'geo_metal186',
                     'geo_metal187',
                     'geo_metal188',
                     'geo_metal189',
                     'geo_metal190',
                     'geo_metal191',
                     'geo_metal192',
                     'geo_metal193',
                     'geo_metal194',
                     'geo_metal195',
                     'geo_metal196',
                     'geo_metal197',
                     'geo_metal198',
                     'geo_metal199',
                     'geo_metal200',
                     'geo_metal201',
                     'geo_metal202',
                     'geo_metal203',
                     'geo_metal204',
                     'geo_metal205',
                     'geo_metal206',
                     'geo_metal207',
                     'geo_metal208',
                     'geo_metal209',
                     'geo_metal210',
                     'geo_metal211',
                     'geo_metal212',
                     'geo_metal213',
                     'geo_metal214',
                     'geo_metal215',
                     'geo_metal216',
                     'geo_metal217',
                     'geo_metal218',
                     'geo_metal219',
                     'geo_metal220',
                     'geo_metal221',
                     'geo_metal222',
                     'geo_metal223',
                     'geo_metal224',
                     'geo_metal225',
                     'geo_metal226',
                     'geo_metal227',
                     'geo_metal228',
                     'geo_metal229',
                     'geo_metal230',
                     'geo_metal231',
                     'geo_metal232',
                     'geo_metal233',
                     'geo_metal234',
                     'geo_metal235',
                     'geo_metal236',
                     'geo_metal237',
                     'geo_metal238',
                     'geo_metal239',
                     'geo_metal240',
                     'geo_metal241',
                     'geo_metal242',
                     'geo_metal243',
                     'geo_metal244',
                     'geo_metal245',
                     'geo_metal246',
                     'geo_metal247',
                     'geo_metal248',
                     'geo_metal249',
                     'geo_metal250',
                     'geo_metal251',
                     'geo_metal252',
                     'geo_metal253',
                     'geo_metal254',
                     'geo_metal255',
                     'geo_metal256',
                     'geo_metal257',
                     'geo_metal258',
                     'geo_metal259',
                     'geo_metal260',
                     'geo_metal261',
                     'geo_metal262',
                     'geo_metal263',
                     'geo_metal264',
                     'geo_metal265',
                     'geo_metal266',
                     'geo_metal267',
                     'geo_metal268',
                     'geo_metal269',
                     'geo_metal270',
                     'geo_metal271',
                     'geo_metal272',
                     'geo_metal273',
                     'geo_metal274',
                     'geo_metal275',
                     'geo_metal276',
                     'geo_metal277',
                     'geo_metal278',
                     'geo_metal279',
                     'geo_metal280',
                     'geo_metal281',
                     'geo_metal282',
                     'geo_metal283',
                     'geo_metal284',
                     'geo_metal285',
                     'geo_metal286',
                     'geo_metal287',
                     'geo_metal288',
                     'geo_metal289',
                     'geo_metal290',
                     'geo_metal291',
                     'geo_metal292',
                     'geo_metal293',
                     'geo_metal294',
                     'geo_metal295',
                     'geo_metal296',
                     'geo_metal297',
                     'geo_rubber_1',
                     'geo_rubber_2',
                     'geo_rubber_3',
                     'geo_rubber_4',
                     'geo_rubber_5',
                     'geo_rubber_6',
                     'geo_rubber_7',
                     'geo_rubber_8',
                     'geo_rubber_9',
                     'geo_rubber_10',
                     'geo_rubber_11',
                     'geo_rubber_12',
                     'geo_rubber_13',
                     'geo_rubber_14',
                     'geo_rubber_15',
                     'geo_rubber_16',
                     'geo_rubber_17',
                     'geo_rubber_18',
                     'geo_rubber_19',
                     'geo_rubber_20',
                     'geo_rubber_21',
                     'geo_plastic1',
                     'geo_plastic2',
                     'geo_plastic3',
                     'geo_plastic4',
                     'geo_plastic5',
                     'geo_plastic6',
                     'geo_plastic7',
                     'geo_plastic8',
                     'geo_plastic12',
                     'geo_plastic11',
                     'geo_plastic10',
                     'geo_plastic9',
                     'geo_metal_60',
                     'geo_metal_353',
                     'geo_metal90',
                     'geo_metal86',
                     'geo_plastic_2',
                     'geo_plastic_1',
                     'geo_metal87',
                     'geo_metal88',
                     'geo_metal91']

    nippersBaseList = ['geo_metal_42',
                        'geo_metal_19',
                        'geo_metal_13',
                        'geo_metal_20',
                        'geo_metal_6',
                        'geo_metal_34',
                        'geo_metal_8',
                        'geo_metal_10',
                        'geo_metal_9',
                        'geo_metal_44',
                        'geo_metal_30',
                        'geo_metal_28',
                        'geo_metal_23',
                        'geo_metal_48',
                        'geo_metal_49',
                        'geo_metal_50',
                        'geo_metal_51',
                        'geo_metal_52',
                        'geo_metal_53',
                        'geo_metal_54',
                        'geo_metal_55',
                        'geo_metal_56',
                        'geo_metal_57',
                        'geo_metal_33',
                        'geo_metal_31',
                        'geo_metal_15',
                        'geo_metal_16',
                        'geo_metal_17',
                        'geo_metal_26',
                        'geo_metal_27',
                        'geo_metal_25',
                        'geo_metal_35',
                        'geo_metal_18',
                        'geo_metal_24',
                        'geo_metal_5',
                        'geo_metal_4',
                        'geo_metal_7',
                        'geo_metal_32',
                        'geo_metal_22',
                        'geo_metal_29',
                        'geo_metal_11',
                        'geo_metal_12',
                        'geo_metal_39',
                        'geo_metal_37',
                        'geo_metal_40',
                        'geo_metal_47',
                        'geo_metal_36',
                        'geo_metal_45',
                        'geo_metal_43',
                        'geo_metal_41',
                        'geo_metal_38',
                        'geo_metal_46',
                        'geo_metal_21',
                        'geo_metal_14',
                        'geo_metal_1',
                        'pHelix1']

    screwdriverBaseList = ['geo_whiteAluminium_1',
                            'geo_whiteAluminium_2',
                            'geo_whiteAluminium_3',
                            'geo_whiteAluminium_4',
                            'geo_whiteAluminium_5',
                            'geo_whiteAluminium_6',
                            'geo_chromeSteel_1',
                            'geo_chromeSteel_2',
                            'geo_chromeSteel_3',
                            'geo_chromeSteel_4',
                            'geo_chromeSteel_5',
                            'geo_darkSteel_1',
                            'geo_darkSteel_2',
                            'geo_darkSteel_3',
                            'geo_darkSteel_4',
                            'geo_darkSteel_5',
                            'geo_darkSteel_6',
                            'geo_greySteel_1',
                            'geo_greySteel_2',
                            'geo_greySteel_3',
                            'geo_greySteel_4',
                            'geo_greySteel_5',
                            'geo_greySteel_6',
                            'geo_greySteel_7',
                            'geo_greySteel_8',
                            'geo_greySteel_9',
                            'geo_greySteel_10',
                            'geo_greySteel_11',
                            'geo_greySteel_12',
                            'geo_greySteel_13',
                            'geo_greySteel_14',
                            'geo_greySteel_15',
                            'geo_greySteel_16',
                            'geo_greySteel_17',
                            'geo_greySteel_18',
                            'geo_greySteel_19',
                            'geo_greySteel_20',
                            'geo_greySteel_21',
                            'geo_greySteel_22',
                            'geo_greySteel_23',
                            'geo_greySteel_24',
                            'geo_greySteel_25',
                            'geo_greySteel_26',
                            'geo_greySteel_27',
                            'geo_redPlastic_1',
                            'geo_redPlastic_2',
                            'geo_darkPlastic_1',
                            'geo_darkPlastic_2',
                            'geo_greySteel_28',
                            'geo_greySteel_29',
                            'geo_greySteel_30',
                            'geo_greySteel_31',
                            'geo_greySteel_32',
                            'geo_greySteel_33',
                            'geo_greySteel_34',
                            'geo_greySteel_35',
                            'geo_greySteel_36',
                            'geo_greySteel_37',
                            'geo_greySteel_38',
                            'geo_greySteel_39',
                            'geo_greySteel_40',
                            'geo_greySteel_41',
                            'geo_greySteel_42',
                            'geo_greySteel_43',
                            'geo_greySteel_44',
                            'geo_greySteel_45',
                            'geo_greySteel_281',
                            'geo_greySteel_291',
                            'geo_greySteel_301',
                            'geo_greySteel_311',
                            'geo_greySteel_321',
                            'geo_greySteel_331',
                            'geo_greySteel_341',
                            'geo_greySteel_351',
                            'geo_greySteel_361',
                            'geo_greySteel_371',
                            'geo_greySteel_381',
                            'geo_greySteel_391',
                            'geo_greySteel_401',
                            'geo_greySteel_411',
                            'geo_greySteel_421',
                            'geo_greySteel_431',
                            'geo_greySteel_441',
                            'geo_greySteel_451',
                            'cloth_v02_polySurface2']

    weldingplateBaseList = ['geo_metal_1',
                            'geo_metal_2',
                            'geo_metal_3',
                            'geo_metal_4',
                            'geo_metal_5',
                            'geo_metal_6',
                            'geo_metal_7',
                            'geo_metal_8',
                            'geo_metal_9',
                            'geo_metal_10',
                            'geo_metal_11',
                            'geo_metal_12',
                            'geo_metal_13',
                            'geo_metal_14',
                            'geo_metal_15',
                            'geo_metal_16',
                            'geo_metal_17',
                            'geo_metal_18',
                            'geo_metal_19',
                            'geo_metal_20',
                            'geo_metal_21',
                            'geo_metal_22',
                            'geo_metal_23',
                            'geo_metal_24',
                            'geo_metal_25',
                            'geo_metal_26',
                            'geo_metal_27',
                            'geo_metal_28',
                            'geo_metal_29',
                            'geo_metal_30',
                            'geo_metal_31',
                            'geo_metal_32',
                            'geo_metal_33',
                            'geo_metal_34',
                            'geo_metal_35',
                            'geo_metal_36',
                            'geo_metal_37',
                            'geo_metal_38',
                            'geo_metal_39',
                            'geo_metal_40',
                            'geo_metal_41',
                            'geo_metal_42',
                            'geo_metal_43',
                            'geo_metal_44',
                            'geo_metal_236',
                            'geo_metal_422',
                            'geo_metal_430',
                            'geo_metal_941',
                            'geo_metal_1201',
                            'geo_metal_1298',
                            'geo_metal_1323',
                            'geo_metal_1482',
                            'geo_metal_1494',
                            'geo_metal_1495',
                            'geo_metal_1496',
                            'geo_metal_1497',
                            'geo_metal_1500',
                            'geo_metal_1501',
                            'geo_metal_1502',
                            'geo_metal_1503',
                            'geo_metal_1505',
                            'geo_metal_1506',
                            'geo_metal_1507',
                            'geo_metal_1508',
                            'geo_metal_1510',
                            'geo_metal_1511',
                            'geo_metal_1512',
                            'geo_metal_1514',
                            'geo_metal_1516',
                            'geo_metal_1517',
                            'geo_metal_1518',
                            'geo_metal_1525',
                            'geo_metal_1526',
                            'geo_metal_1527',
                            'geo_metal_1528',
                            'geo_metal_1529',
                            'geo_metal_1530',
                            'geo_metal_1531',
                            'geo_metal_1532',
                            'geo_metal_1534',
                            'geo_metal_1535',
                            'geo_metal_1536',
                            'geo_metal_1537',
                            'geo_metal_1538',
                            'geo_metal_1540',
                            'geo_metal_1541',
                            'geo_metal_1542',
                            'geo_metal_1543',
                            'geo_metal_1544',
                            'geo_metal_1545',
                            'geo_metal_1546',
                            'geo_metal_1547',
                            'geo_metal_1548',
                            'geo_metal_1549',
                            'geo_metal_1550',
                            'geo_metal_1551',
                            'geo_metal_1552',
                            'geo_metal_1556',
                            'geo_metal_1557',
                            'geo_metal_1558',
                            'geo_metal_1559',
                            'geo_metal_1560',
                            'geo_metal_1561',
                            'geo_metal_1562',
                            'geo_metal_1563',
                            'geo_metal_1564',
                            'geo_metal_1565',
                            'geo_metal_1566']

    weldingplatformBaseList = ['geo_rubber_1',
                               'geo_rubber_2',
                               'geo_rubber_3',
                               'geo_rubber_4',
                               'geo_rubber_5',
                               'geo_metal_2',
                               'geo_metal_3',
                               'geo_metal_4',
                               'geo_metal_5',
                               'geo_metal_6',
                               'geo_metal_7',
                               'geo_metal_8',
                               'geo_metal_9',
                               'geo_metal_10',
                               'geo_metal_11',
                               'geo_metal_12',
                               'geo_metal_13',
                               'geo_metal_14',
                               'geo_metal_15',
                               'geo_metal_16',
                               'geo_metal_17',
                               'geo_metal_18',
                               'geo_metal_19',
                               'geo_metal_20',
                               'geo_metal_21',
                               'geo_metal_22',
                               'geo_metal_23',
                               'geo_metal_24',
                               'geo_metal_25',
                               'geo_metal_26',
                               'geo_metal_27',
                               'geo_metal_28',
                               'geo_metal_29',
                               'geo_metal_30',
                               'geo_metal_31',
                               'geo_metal_32',
                               'geo_metal_33',
                               'geo_metal_34',
                               'geo_metal_35']

    weldingMachineGroupsBaseList = ['grp_welding_machine']

    weldingmachineBaseList = ['geo_metal471',
                                'geo_metal473',
                                'geo_metal477',
                                'geo_metal474',
                                'geo_metal475',
                                'geo_metal478',
                                'geo_metal476',
                                'geo_metal479',
                                'geo_metal472',
                                'geo_metal522',
                                'geo_metal521',
                                'geo_metal525',
                                'geo_glass4',
                                'geo_glass3',
                                'geo_metal560',
                                'geo_metal559',
                                'geo_plastic2',
                                'geo_plastic1',
                                'geo_glass2',
                                'geo_glass1',
                                'geo_metal554',
                                'geo_metal555',
                                'geo_metal556',
                                'geo_metal557',
                                'geo_metal620',
                                'geo_metal619',
                                'geo_metal618',
                                'geo_metal617',
                                'geo_metal616',
                                'geo_metal615',
                                'geo_metal614',
                                'geo_metal611',
                                'geo_metal612',
                                'geo_metal613',
                                'geo_metal610',
                                'geo_metal609',
                                'geo_metal608',
                                'geo_metal607',
                                'geo_metal606',
                                'geo_metal605',
                                'geo_metal597',
                                'geo_metal598',
                                'geo_metal599',
                                'geo_metal600',
                                'geo_metal601',
                                'geo_metal602',
                                'geo_metal603',
                                'geo_metal604',
                                'geo_metal520',
                                'geo_metal519',
                                'geo_metal518',
                                'geo_metal517',
                                'geo_metal512',
                                'geo_metal513',
                                'geo_metal514',
                                'geo_metal515',
                                'geo_metal516',
                                'geo_metal26',
                                'geo_metal25',
                                'geo_metal24',
                                'geo_metal23',
                                'geo_metal22',
                                'geo_metal21',
                                'geo_metal20',
                                'geo_metal13',
                                'geo_metal14',
                                'geo_metal15',
                                'geo_metal16',
                                'geo_metal17',
                                'geo_metal18',
                                'geo_metal19',
                                'geo_metal587',
                                'geo_metal586',
                                'geo_metal585',
                                'geo_metal584',
                                'geo_metal583',
                                'geo_metal582',
                                'geo_metal581',
                                'geo_metal576',
                                'geo_metal577',
                                'geo_metal578',
                                'geo_metal579',
                                'geo_metal580',
                                'geo_metal298',
                                'geo_metal297',
                                'geo_metal296',
                                'geo_metal295',
                                'geo_metal294',
                                'geo_metal293',
                                'geo_metal287',
                                'geo_metal288',
                                'geo_metal289',
                                'geo_metal290',
                                'geo_metal291',
                                'geo_metal292',
                                'geo_metal632',
                                'geo_metal631',
                                'geo_metal630',
                                'geo_metal629',
                                'geo_metal621',
                                'geo_metal622',
                                'geo_metal623',
                                'geo_metal624',
                                'geo_metal625',
                                'geo_metal626',
                                'geo_metal627',
                                'geo_metal628',
                                'geo_metal550',
                                'geo_glass5',
                                'geo_metal548',
                                'geo_metal547',
                                'geo_metal546',
                                'geo_metal542',
                                'geo_metal543',
                                'geo_metal544',
                                'geo_metal545',
                                'geo_metal596',
                                'geo_metal595',
                                'geo_metal594',
                                'geo_metal588',
                                'geo_metal589',
                                'geo_metal590',
                                'geo_metal591',
                                'geo_metal592',
                                'geo_metal593',
                                'geo_metal338',
                                'geo_metal340',
                                'geo_metal339',
                                'geo_metal341',
                                'geo_metal102',
                                'geo_metal104',
                                'geo_metal107',
                                'geo_metal105',
                                'geo_metal108',
                                'geo_metal103',
                                'geo_metal109',
                                'geo_metal106',
                                'geo_metal69',
                                'geo_metal70',
                                'geo_metal64',
                                'geo_metal67',
                                'geo_metal68',
                                'geo_metal65',
                                'geo_metal66',
                                'geo_metal79',
                                'geo_metal78',
                                'geo_metal77',
                                'geo_metal73',
                                'geo_metal75',
                                'geo_metal76',
                                'geo_metal72',
                                'geo_metal74',
                                'geo_metal71',
                                'geo_metal80',
                                'geo_metal91',
                                'geo_metal90',
                                'geo_metal89',
                                'geo_metal88',
                                'geo_metal87',
                                'geo_metal83',
                                'geo_metal84',
                                'geo_metal85',
                                'geo_metal86',
                                'geo_metal114',
                                'geo_metal113',
                                'geo_metal112',
                                'geo_metal111',
                                'geo_metal110',
                                'geo_metal277',
                                'geo_metal286',
                                'geo_metal285',
                                'geo_metal284',
                                'geo_metal283',
                                'geo_metal282',
                                'geo_metal278',
                                'geo_metal276',
                                'geo_metal279',
                                'geo_metal280',
                                'geo_metal281',
                                'geo_metal319',
                                'geo_metal320',
                                'geo_metal315',
                                'geo_metal318',
                                'geo_metal317',
                                'geo_metal314',
                                'geo_metal316',
                                'geo_metal332',
                                'geo_metal331',
                                'geo_metal330',
                                'geo_metal524',
                                'geo_metal526',
                                'geo_metal523',
                                'geo_rubber4',
                                'geo_metal_182',
                                'geo_metal874',
                                'geo_metal871',
                                'geo_metal873',
                                'geo_metal872',
                                'geo_metal870',
                                'geo_metal869',
                                'geo_metal865',
                                'geo_metal864',
                                'geo_plastic_4',
                                'geo_plastic5',
                                'geo_metal902',
                                'geo_metal900',
                                'geo_metal901',
                                'geo_metal898',
                                'geo_metal899',
                                'geo_metal903',
                                'geo_metal6',
                                'geo_metal5',
                                'geo_metal4',
                                'geo_metal3',
                                'geo_metal2',
                                'geo_metal1',
                                'geo_metal7',
                                'geo_metal8',
                                'geo_metal9',
                                'geo_metal10',
                                'geo_metal12',
                                'geo_metal11',
                                'geo_metal52',
                                'geo_cloth2',
                                'geo_metal53',
                                'geo_metal54',
                                'geo_plastic3',
                                'geo_plastic_3',
                                'geo_metal81',
                                'geo_metal82',
                                'geo_plastic4',
                                'geo_plastic_2',
                                'geo_metal118',
                                'geo_metal117',
                                'geo_metal116',
                                'geo_metal115',
                                'geo_metal124',
                                'geo_metal123',
                                'geo_metal122',
                                'geo_metal121',
                                'geo_metal120',
                                'geo_metal119',
                                'geo_metal32',
                                'geo_metal33',
                                'geo_metal37',
                                'geo_metal38',
                                'geo_metal39',
                                'geo_metal307',
                                'geo_metal308',
                                'geo_metal309',
                                'geo_metal310',
                                'geo_metal311',
                                'geo_metal312',
                                'geo_metal313',
                                'geo_metal335',
                                'geo_metal333',
                                'geo_metal334',
                                'geo_metal336',
                                'geo_metal337',
                                'geo_metal368',
                                'geo_metal369',
                                'geo_metal370',
                                'geo_metal375',
                                'geo_metal374',
                                'geo_metal371',
                                'geo_metal373',
                                'geo_metal372',
                                'geo_metal367',
                                'geo_metal366',
                                'geo_metal365',
                                'geo_metal364',
                                'geo_metal363',
                                'geo_metal362',
                                'geo_metal402',
                                'geo_metal410',
                                'geo_metal404',
                                'geo_metal406',
                                'geo_metal408',
                                'geo_metal403',
                                'geo_metal405',
                                'geo_metal407',
                                'geo_metal411',
                                'geo_metal409',
                                'geo_metal421',
                                'geo_metal422',
                                'geo_metal423',
                                'geo_metal424',
                                'geo_metal425',
                                'geo_metal415',
                                'geo_metal414',
                                'geo_metal413',
                                'geo_metal412',
                                'geo_metal420',
                                'geo_metal426',
                                'geo_metal419',
                                'geo_metal418',
                                'geo_metal417',
                                'geo_metal416',
                                'geo_metal437',
                                'geo_metal438',
                                'geo_metal439',
                                'geo_metal440',
                                'geo_metal443',
                                'geo_metal442',
                                'geo_metal441',
                                'geo_metal892',
                                'geo_metal891',
                                'geo_metal890',
                                'geo_metal889',
                                'geo_metal888',
                                'geo_rubber10',
                                'geo_metal886',
                                'geo_metal885',
                                'geo_metal884',
                                'geo_metal893',
                                'geo_metal894',
                                'geo_metall',
                                'geo_metal895',
                                'geo_metal896',
                                'geo_metal897',
                                'geo_metal490',
                                'geo_metal491',
                                'geo_metal492',
                                'geo_metal493',
                                'geo_metal483',
                                'geo_plastic_1',
                                'geo_metal482',
                                'geo_metal481',
                                'geo_metal489',
                                'geo_metal488',
                                'geo_metal487',
                                'geo_metal486',
                                'geo_metal485',
                                'geo_metal494',
                                'geo_metal484',
                                'geo_metal511',
                                'geo_plastic_5',
                                'geo_metal507',
                                'geo_metal508',
                                'geo_metal574',
                                'geo_metal575',
                                'geo_plastic6',
                                'geo_metal567',
                                'geo_metal563',
                                'geo_metal569',
                                'geo_metal566',
                                'geo_metal565',
                                'geo_metal573',
                                'geo_metal572',
                                'geo_metal828',
                                'geo_metal829',
                                'geo_metal830',
                                'geo_metal831',
                                'geo_metal832',
                                'geo_metal833',
                                'geo_metal834',
                                'geo_metal835',
                                'geo_metal836',
                                'geo_metal837',
                                'geo_metal838',
                                'geo_metal839',
                                'geo_metal840',
                                'geo_metal814',
                                'geo_metal790',
                                'geo_rubber9',
                                'geo_metal791',
                                'geo_metal792',
                                'geo_metal793',
                                'geo_metal794',
                                'geo_metal795',
                                'geo_metal796',
                                'geo_metal797',
                                'geo_metal769',
                                'geo_metal770',
                                'geo_metal771',
                                'geo_metal772',
                                'geo_metal773',
                                'geo_metal774',
                                'geo_metal708',
                                'geo_metal709',
                                'geo_metal710',
                                'geo_metal711',
                                'geo_metal712',
                                'geo_metal713',
                                'geo_metal714',
                                'geo_metal715',
                                'geo_metal716',
                                'geo_metal717',
                                'geo_metal718',
                                'geo_metal719',
                                'geo_metal720',
                                'geo_metal721',
                                'geo_metal722',
                                'geo_metal692',
                                'geo_metal693',
                                'geo_metal694',
                                'geo_metal695',
                                'geo_metal696',
                                'geo_metal697',
                                'geo_metal698',
                                'geo_metal699',
                                'geo_metal700',
                                'geo_metal701',
                                'geo_metal702',
                                'geo_metal703',
                                'geo_metal704',
                                'geo_metal705',
                                'geo_metal706',
                                'geo_metal677',
                                'geo_metal667',
                                'geo_metal668',
                                'geo_metal669',
                                'geo_metal670',
                                'geo_metal671',
                                'geo_metal672',
                                'geo_metal673',
                                'geo_metal674',
                                'geo_metal675',
                                'geo_metal676',
                                'geo_metal815',
                                'geo_metal816',
                                'geo_metal461',
                                'geo_metal469',
                                'geo_metal463',
                                'geo_metal468',
                                'geo_metal464',
                                'geo_metal350',
                                'geo_metal351',
                                'geo_metal299',
                                'geo_metal305',
                                'geo_metal306',
                                'geo_metal302',
                                'geo_metal635',
                                'geo_metal644',
                                'geo_metal636',
                                'geo_metal634',
                                'geo_metal633',
                                'geo_metal571',
                                'geo_metal568',
                                'geo_metal564',
                                'geo_metal570',
                                'geo_metal661',
                                'geo_metal660',
                                'geo_metal659',
                                'geo_metal658',
                                'geo_metal657',
                                'geo_metal656',
                                'geo_metal655',
                                'geo_metal654',
                                'geo_metal653',
                                'geo_metal652',
                                'geo_metal651',
                                'geo_metal650',
                                'geo_metal649',
                                'geo_metal648',
                                'geo_metal647',
                                'geo_metal646',
                                'geo_metal666',
                                'geo_metal665',
                                'geo_metal664',
                                'geo_metal663',
                                'geo_metal662',
                                'geo_metal691',
                                'geo_metal690',
                                'geo_metal689',
                                'geo_metal688',
                                'geo_metal687',
                                'geo_metal686',
                                'geo_metal685',
                                'geo_metal684',
                                'geo_metal683',
                                'geo_rubber1',
                                'geo_metal682',
                                'geo_metal681',
                                'geo_metal680',
                                'geo_metal679',
                                'geo_metal678',
                                'geo_metal707',
                                'geo_metal737',
                                'geo_metal736',
                                'geo_metal735',
                                'geo_metal734',
                                'geo_metal733',
                                'geo_metal732',
                                'geo_metal731',
                                'geo_metal730',
                                'geo_metal729',
                                'geo_metal728',
                                'geo_metal727',
                                'geo_metal726',
                                'geo_metal725',
                                'geo_metal724',
                                'geo_metal723',
                                'geo_metal753',
                                'geo_metal752',
                                'geo_metal751',
                                'geo_metal750',
                                'geo_metal749',
                                'geo_metal748',
                                'geo_metal747',
                                'geo_metal746',
                                'geo_metal745',
                                'geo_metal744',
                                'geo_metal743',
                                'geo_metal742',
                                'geo_metal741',
                                'geo_metal740',
                                'geo_metal739',
                                'geo_metal738',
                                'geo_metal768',
                                'geo_metal767',
                                'geo_metal766',
                                'geo_metal765',
                                'geo_metal764',
                                'geo_metal763',
                                'geo_metal762',
                                'geo_metal761',
                                'geo_metal760',
                                'geo_metal759',
                                'geo_metal758',
                                'geo_metal757',
                                'geo_metal756',
                                'geo_metal755',
                                'geo_metal754',
                                'geo_metal784',
                                'geo_metal783',
                                'geo_metal782',
                                'geo_metal781',
                                'geo_metal780',
                                'geo_metal779',
                                'geo_metal778',
                                'geo_metal777',
                                'geo_metal776',
                                'geo_metal775',
                                'geo_rubber3',
                                'geo_metal789',
                                'geo_metal788',
                                'geo_metal787',
                                'geo_metal786',
                                'geo_metal785',
                                'geo_metal813',
                                'geo_metal812',
                                'geo_metal811',
                                'geo_metal810',
                                'geo_metal809',
                                'geo_metal808',
                                'geo_metal807',
                                'geo_metal806',
                                'geo_metal805',
                                'geo_metal804',
                                'geo_metal803',
                                'geo_metal802',
                                'geo_metal801',
                                'geo_metal800',
                                'geo_metal799',
                                'geo_metal798',
                                'geo_metal827',
                                'geo_metal826',
                                'geo_metal825',
                                'geo_metal824',
                                'geo_metal823',
                                'geo_rubber2',
                                'geo_metal822',
                                'geo_metal821',
                                'geo_metal820',
                                'geo_metal819',
                                'geo_metal818',
                                'geo_metal817',
                                'geo_cloth',
                                'geo_cloth_3',
                                'geo_cloth_1',
                                'geo_cloth_2',
                                'geo_metal906',
                                'geo_metal907',
                                'geo_metal908',
                                'geo_metal909',
                                'geo_metal910',
                                'geo_metal911',
                                'geo_metal912',
                                'geo_metal913',
                                'geo_metal914',
                                'geo_metal915',
                                'geo_metal916',
                                'geo_metal917',
                                'geo_metal918',
                                'geo_metal919',
                                'geo_metal920',
                                'geo_metal921',
                                'geo_metal922',
                                'geo_metal923',
                                'geo_metal924',
                                'geo_metal925',
                                'geo_metal926',
                                'geo_metal927',
                                'geo_metal928',
                                'geo_metal929',
                                'geo_metal931',
                                'geo_metal932',
                                'geo_metal933',
                                'geo_metal934',
                                'geo_metal935',
                                'geo_metal936',
                                'geo_metal937',
                                'geo_metal938',
                                'geo_metal939',
                                'geo_metal940',
                                'geo_metal941',
                                'geo_metal942',
                                'geo_metal943',
                                'geo_metal944',
                                'geo_metal945',
                                'geo_metal946',
                                'geo_metal947',
                                'geo_metal948',
                                'geo_metal949',
                                'geo_metal950',
                                'geo_metal951',
                                'geo_metal952',
                                'geo_metal953',
                                'geo_metal954',
                                'geo_metal955',
                                'geo_metal956',
                                'geo_metal957',
                                'geo_metal958',
                                'geo_metal959',
                                'geo_metal960',
                                'geo_metal961',
                                'geo_metal962',
                                'geo_metal963',
                                'geo_metal964',
                                'geo_metal965',
                                'geo_metal966',
                                'geo_metal967',
                                'geo_metal968',
                                'geo_metal969',
                                'geo_metal970',
                                'geo_metal972',
                                'geo_metal976',
                                'geo_metal977',
                                'geo_metal979',
                                'geo_metal981',
                                'geo_metal982',
                                'geo_metal983',
                                'geo_metal984',
                                'geo_metal985',
                                'geo_metal986',
                                'geo_metal987',
                                'geo_metal988',
                                'geo_metal989',
                                'geo_metal990',
                                'geo_metal991',
                                'geo_metal992',
                                'geo_metal993',
                                'geo_metal994',
                                'geo_metal995',
                                'geo_metal996',
                                'geo_metal997',
                                'geo_metal998',
                                'geo_metal999',
                                'geo_metal1000',
                                'geo_metal1001',
                                'geo_metal1002',
                                'geo_metal1003',
                                'geo_metal1004',
                                'geo_metal1005',
                                'geo_metal1006',
                                'geo_metal1007',
                                'geo_metal1008',
                                'geo_metal1009',
                                'geo_metal1010',
                                'geo_metal1011',
                                'geo_metal1012',
                                'geo_metal1013',
                                'geo_metal1014',
                                'geo_metal1015',
                                'geo_metal1016',
                                'geo_metal1017',
                                'geo_metal1018',
                                'geo_metal1019',
                                'geo_metal1020',
                                'geo_metal1021',
                                'geo_metal1022',
                                'geo_metal1023',
                                'geo_metal1024',
                                'geo_metal1025',
                                'geo_metal1026',
                                'geo_metal1027',
                                'geo_metal1028',
                                'geo_metal1029',
                                'geo_metal1030',
                                'geo_metal1031',
                                'geo_metal1032',
                                'geo_metal1033',
                                'geo_metal1034',
                                'geo_metal1035',
                                'geo_metal1036',
                                'geo_metal1037',
                                'geo_metal1038',
                                'geo_metal1039',
                                'geo_metal1040',
                                'geo_metal1041',
                                'geo_metal1042',
                                'geo_metal1043',
                                'geo_metal1044',
                                'geo_metal1045',
                                'geo_metal1046',
                                'geo_metal1047',
                                'geo_metal1048',
                                'geo_metal1049',
                                'geo_metal1050',
                                'geo_metal1051',
                                'geo_metal1052',
                                'geo_metal1053',
                                'geo_metal1054',
                                'geo_metal1055',
                                'geo_metal1056',
                                'geo_metal1057',
                                'geo_metal1058',
                                'geo_metal1059',
                                'geo_metal1060',
                                'geo_metal1061',
                                'geo_metal1062',
                                'geo_metal1063',
                                'geo_metal1064',
                                'geo_metal1065',
                                'geo_metal1066',
                                'geo_metal1067',
                                'geo_metal1068',
                                'geo_metal1069',
                                'geo_metal1070',
                                'geo_metal1071',
                                'geo_metal1072',
                                'geo_metal1073',
                                'geo_metal1074',
                                'geo_metal1075',
                                'geo_metal1076',
                                'geo_metal1077',
                                'geo_metal1078',
                                'geo_metal1079',
                                'geo_metal1080',
                                'geo_metal1081',
                                'geo_metal1082',
                                'geo_metal1083',
                                'geo_metal1084',
                                'geo_metal1085',
                                'geo_metal1086',
                                'geo_metal1087',
                                'geo_metal1088',
                                'geo_metal1089',
                                'geo_metal1090',
                                'geo_metal1091',
                                'geo_metal1092',
                                'geo_metal1093',
                                'geo_metal1094',
                                'geo_metal1095',
                                'geo_metal1096',
                                'geo_metal1097',
                                'geo_metal1098',
                                'geo_metal1099',
                                'geo_metal1100',
                                'geo_metal1101',
                                'geo_metal1102',
                                'geo_metal1103',
                                'geo_metal1104',
                                'geo_metal1105',
                                'geo_metal1106',
                                'geo_metal1107',
                                'geo_metal1108',
                                'geo_metal1109',
                                'geo_metal1110',
                                'geo_metal1111',
                                'geo_metal1112',
                                'geo_metal1113',
                                'geo_metal1114',
                                'geo_metal1115',
                                'geo_metal1116',
                                'geo_metal1117',
                                'geo_metal1118',
                                'geo_metal1119',
                                'geo_metal1120',
                                'geo_metal1121',
                                'geo_metal1122',
                                'geo_metal1123',
                                'geo_metal1124',
                                'geo_metal1125',
                                'geo_metal1126',
                                'geo_metal1127',
                                'geo_metal1128',
                                'geo_metal1129',
                                'geo_metal1130',
                                'geo_metal1131',
                                'geo_metal1132',
                                'geo_metal1133',
                                'geo_metal1134',
                                'geo_metal1135',
                                'geo_metal1136',
                                'geo_metal1137',
                                'geo_metal1138',
                                'geo_metal1139',
                                'geo_metal1140',
                                'geo_metal1141',
                                'geo_metal1142',
                                'geo_metal1143',
                                'geo_metal1144',
                                'geo_metal1145',
                                'geo_metal1146',
                                'geo_metal1147',
                                'geo_metal1148',
                                'geo_metal1151',
                                'geo_metal1152',
                                'geo_metal1153',
                                'geo_metal1154',
                                'geo_metal1155',
                                'geo_metal1156',
                                'geo_metal1157',
                                'geo_metal1158',
                                'geo_metal1159',
                                'geo_metal1160',
                                'geo_metal1161',
                                'geo_metal1162',
                                'geo_metal1163',
                                'geo_metal1164',
                                'geo_metal1165',
                                'geo_metal1166',
                                'geo_metal1167',
                                'geo_metal1168',
                                'geo_metal1169',
                                'geo_metal1170',
                                'geo_metal1171',
                                'geo_metal1172',
                                'geo_metal1173',
                                'geo_metal1174',
                                'geo_metal1175',
                                'geo_metal1176',
                                'geo_metal1177',
                                'geo_metal1178',
                                'geo_metal1179',
                                'geo_metal1180',
                                'geo_metal1181',
                                'geo_metal1182',
                                'geo_metal1183',
                                'geo_metal1184',
                                'geo_metal1185',
                                'geo_metal1186',
                                'geo_metal1187',
                                'geo_metal1188',
                                'geo_metal1189',
                                'geo_metal1190',
                                'geo_metal1191',
                                'geo_metal1192',
                                'geo_metal1193',
                                'geo_metal1194',
                                'geo_metal1195',
                                'geo_metal1196',
                                'geo_metal1197',
                                'geo_metal1198',
                                'geo_metal1199',
                                'geo_metal1200',
                                'geo_metal1201',
                                'geo_metal1202',
                                'geo_metal1203',
                                'geo_metal1204',
                                'geo_metal1205',
                                'geo_metal1206',
                                'geo_metal1207',
                                'geo_metal1208',
                                'geo_metal1209',
                                'geo_metal1210',
                                'geo_metal1211',
                                'geo_metal1212',
                                'geo_metal1213',
                                'geo_metal1214',
                                'geo_metal1215',
                                'geo_metal1216',
                                'geo_metal1217',
                                'geo_metal1218',
                                'geo_metal1219',
                                'geo_metal1220',
                                'geo_metal1221',
                                'geo_metal1222',
                                'geo_metal1223',
                                'geo_metal1224',
                                'geo_metal1225',
                                'geo_metal1227',
                                'geo_metal1228',
                                'geo_metal1229',
                                'geo_metal1230',
                                'geo_metal1231',
                                'geo_metal1232',
                                'geo_metal1233',
                                'geo_metal1234',
                                'geo_metal1235',
                                'geo_metal1236',
                                'geo_metal1237',
                                'geo_metal1238',
                                'geo_metal1239',
                                'geo_metal1240',
                                'geo_metal1241',
                                'geo_metal1242',
                                'geo_metal1243',
                                'geo_metal1244',
                                'geo_metal1245',
                                'geo_metal1246',
                                'geo_metal1247',
                                'geo_metal1248',
                                'geo_metal1249',
                                'geo_metal1250',
                                'geo_metal1251',
                                'geo_metal1252',
                                'geo_metal1253',
                                'geo_metal1254',
                                'geo_metal1255',
                                'geo_metal1256',
                                'geo_metal1257',
                                'geo_metal1258',
                                'geo_metal1259',
                                'geo_metal1260',
                                'geo_metal1261',
                                'geo_metal1262',
                                'geo_metal975',
                                'geo_metal978',
                                'geo_metal980',
                                'geo_metal1149',
                                'geo_metal1150',
                                'geo_metal1226',
                                'geo_metal974',
                                'geo_metal930',
                                'geo_metal973',
                                'geo_metal971',
                                'geo_mount_17',
                                'geo_mount_3',
                                'geo_mount_2',
                                'geo_mount_1',
                                'geo_mount_4',
                                'geo_mount_38',
                                'geo_mount_35',
                                'geo_mount_36',
                                'geo_mount_37',
                                'geo_mount_31',
                                'geo_metal_mount_12',
                                'geo_metal_mount_13',
                                'geo_metal_mount_14',
                                'geo_metal_mount_20',
                                'geo_metal_mount_19',
                                'geo_metal_mount_18',
                                'geo_metal_mount_16',
                                'geo_metal_mount_15',
                                'geo_metal_mount_11',
                                'geo_metal_mount_21',
                                'geo_metal_mount_22',
                                'geo_metal_mount_24',
                                'geo_metal_mount_41',
                                'geo_metal_mount_34',
                                'geo_metal_mount_39',
                                'geo_metal_mount_33',
                                'geo_metal_mount_5',
                                'geo_metal_mount_10',
                                'geo_metal_mount_9',
                                'geo_metal_mount_8',
                                'geo_metal_mount_7',
                                'geo_metal_mount_6',
                                'geo_metal_mount_26',
                                'geo_metal_mount_29',
                                'geo_metal_mount_32',
                                'geo_metal_mount_30',
                                'geo_metal_mount_27',
                                'geo_metal_mount_28',
                                'geo_plastic_mount_40',
                                'geo_rubber_mount_23',
                                'geo_rubber_mount_25']

    paneltoolBaseList = ['geo_metall_830',
                         'geo_metall_829',
                         'geo_metall_828',
                         'geo_metall_827',
                         'geo_metall_826',
                         'geo_metall_825',
                         'geo_metall_824',
                         'geo_metall_823',
                         'geo_metall_822',
                         'geo_metall_790',
                         'geo_metall_789',
                         'geo_metall_788',
                         'geo_metall_793',
                         'geo_metall_792',
                         'geo_metall_798',
                         'geo_metall_796',
                         'geo_metall_794',
                         'geo_metall_801',
                         'geo_metall_800',
                         'geo_metall_799',
                         'geo_metall_797',
                         'geo_metall_795',
                         'geo_metall_802',
                         'geo_metall_3',
                         'geo_metall_2',
                         'geo_metall_1',
                         'geo_metall_4',
                         'geo_plastic_4',
                         'geo_plastic_3',
                         'geo_plastic_1',
                         'geo_plastic_2',
                         'geo_plastic_5',
                         'geo_plastic_15',
                         'geo_plastic_16',
                         'geo_plastic_12',
                         'geo_plastic_13',
                         'geo_plastic_14',
                         'geo_metall_815',
                         'geo_metall_717',
                         'geo_metall_716',
                         'geo_metall_715',
                         'geo_metall_747',
                         'geo_metall_746',
                         'geo_metall_743',
                         'geo_metall_744',
                         'geo_metall_745',
                         'geo_metall_694',
                         'geo_metall_692',
                         'geo_metall_691',
                         'geo_metall_689',
                         'geo_metall_688',
                         'geo_metall_686',
                         'geo_metall_687',
                         'geo_metall_690',
                         'geo_metall_693',
                         'geo_metall_763',
                         'geo_metall_764',
                         'geo_metall_768',
                         'geo_metall_767',
                         'geo_metall_769',
                         'geo_metall_776',
                         'geo_metall_777',
                         'geo_metall_778',
                         'geo_metall_779',
                         'geo_metall_780',
                         'geo_metall_781',
                         'geo_metall_782',
                         'geo_metall_685',
                         'geo_metall_684',
                         'geo_metall_682',
                         'geo_metall_681',
                         'geo_metall_679',
                         'geo_metall_677',
                         'geo_metall_678',
                         'geo_metall_680',
                         'geo_metall_683',
                         'geo_metall_673',
                         'geo_metall_670',
                         'geo_metall_672',
                         'geo_metall_671',
                         'geo_metall_669',
                         'geo_metall_666',
                         'geo_metall_665',
                         'geo_metall_668',
                         'geo_metall_5',
                         'geo_metall_667',
                         'geo_metall_735',
                         'geo_metall_736',
                         'geo_metall_698',
                         'geo_metall_697',
                         'geo_metall_696',
                         'geo_metall_695',
                         'geo_metall_791',
                         'geo_metall_787',
                         'geo_metall_784',
                         'geo_metall_786',
                         'geo_metall_783',
                         'geo_metall_785',
                         'geo_metall_712',
                         'geo_metall_714',
                         'geo_metall_718',
                         'geo_metall_721',
                         'geo_metall_720',
                         'geo_metall_719',
                         'geo_metall_701',
                         'geo_metall_702',
                         'geo_metall_700',
                         'geo_metall_699',
                         'geo_metall_730',
                         'geo_metall_729',
                         'geo_metall_728',
                         'geo_metall_813',
                         'geo_metall_814',
                         'geo_metall_766',
                         'geo_metall_765',
                         'geo_metall_727',
                         'geo_metall_726',
                         'geo_plastic_11',
                         'geo_plastic_10',
                         'geo_metall_811',
                         'geo_metall_810',
                         'geo_metall_812',
                         'geo_metall_723',
                         'geo_metall_722',
                         'geo_metall_770',
                         'geo_metall_775',
                         'geo_metall_772',
                         'geo_metall_771',
                         'geo_metall_724',
                         'geo_metall_725',
                         'geo_metall_773',
                         'geo_metall_774',
                         'geo_metall_750',
                         'geo_metall_752',
                         'geo_metall_751',
                         'geo_metall_758',
                         'geo_metall_761',
                         'geo_metall_756',
                         'geo_metall_741',
                         'geo_metall_737',
                         'geo_metall_731',
                         'geo_plastic_6',
                         'geo_metall_733',
                         'geo_metall_732',
                         'geo_metall_762',
                         'geo_metall_759',
                         'geo_metall_760',
                         'geo_metall_674',
                         'geo_metall_675',
                         'geo_metall_676',
                         'geo_metall_809',
                         'geo_plastic_9',
                         'geo_metall_804',
                         'geo_metall_803',
                         'geo_metall_806',
                         'geo_metall_807',
                         'geo_metall_808',
                         'geo_metall_805',
                         'geo_metall_843',
                         'geo_metall_839',
                         'geo_metall_837',
                         'geo_metall_840',
                         'geo_metall_831',
                         'geo_metall_832',
                         'geo_metall_851',
                         'geo_metall_850',
                         'geo_metall_849',
                         'geo_metall_848',
                         'geo_metall_847',
                         'geo_metall_846',
                         'geo_metall_742',
                         'geo_metall_739',
                         'geo_metall_740',
                         'geo_metall_734',
                         'geo_metall_738',
                         'geo_metall_705',
                         'geo_metall_703',
                         'geo_metall_706',
                         'geo_metall_708',
                         'geo_metall_710',
                         'geo_metall_711',
                         'geo_metall_704',
                         'geo_metall_707',
                         'geo_metall_709',
                         'geo_metall_713',
                         'geo_metall_841',
                         'geo_metall_838',
                         'geo_metall_836',
                         'geo_metall_834',
                         'geo_metall_844',
                         'geo_metall_833',
                         'geo_metall_835',
                         'geo_metall_845',
                         'geo_metall_842',
                         'geo_metall_817',
                         'geo_metall_816',
                         'geo_metall_818',
                         'geo_metall_819',
                         'geo_plastic_7',
                         'geo_metall_749',
                         'geo_metall_748',
                         'geo_metall_820',
                         'geo_metall_821',
                         'geo_metall_755',
                         'geo_metall_757',
                         'geo_plastic_8',
                         'geo_metall_754',
                         'geo_metall_753']

    beltBaseList = ['geo_metal_0447',
                    'geo_metal_0448',
                    'geo_metal_0460',
                    'geo_metal_0461',
                    'geo_metal_0463',
                    'geo_cloth_044',
                    'geo_metal_0476',
                    'geo_metal_0477',
                    'geo_metal_0478',
                    'geo_metal_0479',
                    'geo_metal_0480',
                    'geo_cloth_048',
                    'geo_metal_0449',
                    'geo_metal_0450',
                    'geo_metal_0451',
                    'geo_metal_0452',
                    'geo_metal_0453',
                    'geo_metal_0454',
                    'geo_metal_0455',
                    'geo_metal_0456',
                    'geo_metal_0457',
                    'geo_metal_0458',
                    'geo_metal_0459',
                    'geo_metal_0462',
                    'geo_metal_0481',
                    'geo_metal_0482',
                    'geo_metal_0483',
                    'geo_metal_0484',
                    'geo_metal_0485',
                    'geo_metal_0486',
                    'geo_metal_0487',
                    'geo_metal_0488',
                    'geo_metal_0489',
                    'geo_metal_0490',
                    'geo_metal_0491',
                    'geo_metal_0492',
                    'geo_metal_0413',
                    'geo_metal_0416',
                    'geo_metal_0415',
                    'geo_metal_0411',
                    'geo_metal_0414',
                    'geo_metal_0412']


    def __init__(self):
        super(salutAbcExport, self).__init__()
        self.setupUi()

    def setupUi(self):
        # -------------------------------------GUI WIDGETS-----------------------------
        # -- ORLAN D SETUP : --
        self.orlanDlamp = QtGui.QLabel('')
        self.orlanDlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.orlanDlamp.setFixedWidth(32)
        self.orlanDlabel = QtGui.QLabel('ORLAN namespace D')
        self.orlanDExportBtn = QtGui.QPushButton('Export >>')
        self.orlanDExportBtn.setEnabled(False)

        # -- ORLAN S SETUP : --
        self.orlanSlamp = QtGui.QLabel('')
        self.orlanSlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.orlanSlamp.setFixedWidth(32)
        self.orlanSlabel = QtGui.QLabel('ORLAN namespace S')
        self.orlanSExportBtn = QtGui.QPushButton('Export >>')
        self.orlanSExportBtn.setEnabled(False)

        # -- ANCHOR A SETUP : --
        self.anchorAlamp = QtGui.QLabel('')
        self.anchorAlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.anchorAlamp.setFixedWidth(32)
        self.anchorAlabel = QtGui.QLabel('ANCHOR namespace A')
        self.anchorAExportBtn = QtGui.QPushButton('Export >>')
        self.anchorAExportBtn.setEnabled(False)

        # -- ANCHOR A2 SETUP : --
        self.anchorA2lamp = QtGui.QLabel('')
        self.anchorA2lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.anchorA2lamp.setFixedWidth(32)
        self.anchorA2label = QtGui.QLabel('ANCHOR namespace A2')
        self.anchorA2ExportBtn = QtGui.QPushButton('Export >>')
        self.anchorA2ExportBtn.setEnabled(False)

        # -- CAMERA C SETUP : --
        self.cameraClamp = QtGui.QLabel('')
        self.cameraClamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.cameraClamp.setFixedWidth(32)
        self.cameraClabel = QtGui.QLabel('CAMERA namespace C')
        self.cameraCExportBtn = QtGui.QPushButton('Export >>')
        self.cameraCExportBtn.setEnabled(False)

        # -- HATCH H SETUP : --
        self.hatchHlamp = QtGui.QLabel('')
        self.hatchHlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.hatchHlamp.setFixedWidth(32)
        self.hatchHlabel = QtGui.QLabel('HATCH namespace H')
        self.hatchHExportBtn = QtGui.QPushButton('Export >>')
        self.hatchHExportBtn.setEnabled(False)

        # -- NIPPERS N SETUP : --
        self.nippersNlamp = QtGui.QLabel('')
        self.nippersNlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.nippersNlamp.setFixedWidth(32)
        self.nippersNlabel = QtGui.QLabel('NIPPERS namespace N')
        self.nippersNExportBtn = QtGui.QPushButton('Export >>')
        self.nippersNExportBtn.setEnabled(False)

        # -- WELDINGPLATE WP SETUP : --
        self.weldingplateWPlamp = QtGui.QLabel('')
        self.weldingplateWPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.weldingplateWPlamp.setFixedWidth(32)
        self.weldingplateWPlabel = QtGui.QLabel('WELDING_PLATE namespace WP')
        self.weldingplateWPExportBtn = QtGui.QPushButton('Export >>')
        self.weldingplateWPExportBtn.setEnabled(False)

        # -- HAMMER P SETUP : --
        self.hammerPlamp = QtGui.QLabel('')
        self.hammerPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.hammerPlamp.setFixedWidth(32)
        self.hammerPlabel = QtGui.QLabel('HAMMER namespace P')
        self.hammerPExportBtn = QtGui.QPushButton('Export >>')
        self.hammerPExportBtn.setEnabled(False)

        # -- SCREW P SETUP : --
        self.screwPlamp = QtGui.QLabel('')
        self.screwPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.screwPlamp.setFixedWidth(32)
        self.screwPlabel = QtGui.QLabel('SCREWDRIVER namespace P')
        self.screwPExportBtn = QtGui.QPushButton('Export >>')
        self.screwPExportBtn.setEnabled(False)

        # -- WELDINGPLATFORM WPM SETUP : --
        self.weldingplatformWPMlamp = QtGui.QLabel('')
        self.weldingplatformWPMlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.weldingplatformWPMlamp.setFixedWidth(32)
        self.weldingplatformWPMlabel = QtGui.QLabel('WELDING_PLATFORM namespace WPM')
        self.weldingplatformWPMExportBtn = QtGui.QPushButton('Export >>')
        self.weldingplatformWPMExportBtn.setEnabled(False)

        # -- WELDINGMACHIVE WM SETUP : --
        self.weldingmachineWMlamp = QtGui.QLabel('')
        self.weldingmachineWMlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.weldingmachineWMlamp.setFixedWidth(32)
        self.weldingmachineWMlabel = QtGui.QLabel('WELDING_MACHINE namespace WM')
        self.weldingmachineWMExportBtn = QtGui.QPushButton('Export >>')
        self.weldingmachineWMExportBtn.setEnabled(False)

        # -- PANELTOOL P SETUP : --
        self.paneltoolPlamp = QtGui.QLabel('')
        self.paneltoolPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.paneltoolPlamp.setFixedWidth(32)
        self.paneltoolPlabel = QtGui.QLabel('PANEL_TOOL namespace P')
        self.paneltoolPExportBtn = QtGui.QPushButton('Export >>')
        self.paneltoolPExportBtn.setEnabled(False)

        # -- BELT1 B1 SETUP : --
        self.beltB1lamp = QtGui.QLabel('')
        self.beltB1lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.beltB1lamp.setFixedWidth(32)
        self.beltB1label = QtGui.QLabel('BELT1 namespace B1')
        self.beltB1ExportBtn = QtGui.QPushButton('Export >>')
        self.beltB1ExportBtn.setEnabled(False)

        # -- BELT1 B2 SETUP : --
        self.beltB2lamp = QtGui.QLabel('')
        self.beltB2lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
        self.beltB2lamp.setFixedWidth(32)
        self.beltB2label = QtGui.QLabel('BELT2 namespace B2')
        self.beltB2ExportBtn = QtGui.QPushButton('Export >>')
        self.beltB2ExportBtn.setEnabled(False)

        # -- Refresh Button : --
        self.refreshBtn = QtGui.QPushButton('REFRESH')
        self.refreshBtn.setFixedHeight(64)
        self.refreshBtn.setIcon(QtGui.QIcon(QtGui.QPixmap('/prefs/maya/icons/Refresh.png')))
        self.refreshBtn.setIconSize(QtCore.QSize(48, 48))

        # -- Out Log : --
        self.outLog = QtGui.QTextEdit()
        self.outLog.setFixedHeight(450)

        # -------------------------------------LAYOUT SETUP-----------------------------
        gbox = QtGui.QGridLayout()
        #add orlan D
        gbox.addWidget(self.orlanDlamp, 0, 1)
        gbox.addWidget(self.orlanDlabel, 0, 2)
        gbox.addWidget(self.orlanDExportBtn, 0, 3)

        # add orlan S
        gbox.addWidget(self.orlanSlamp, 1, 1)
        gbox.addWidget(self.orlanSlabel, 1, 2)
        gbox.addWidget(self.orlanSExportBtn, 1, 3)

        # add anchor a
        gbox.addWidget(self.anchorAlamp, 2, 1)
        gbox.addWidget(self.anchorAlabel, 2, 2)
        gbox.addWidget(self.anchorAExportBtn, 2, 3)

        # add anchor a2
        gbox.addWidget(self.anchorA2lamp, 3, 1)
        gbox.addWidget(self.anchorA2label, 3, 2)
        gbox.addWidget(self.anchorA2ExportBtn, 3, 3)

        # add camera C
        gbox.addWidget(self.cameraClamp, 4, 1)
        gbox.addWidget(self.cameraClabel, 4, 2)
        gbox.addWidget(self.cameraCExportBtn, 4, 3)

        #add hatch H
        gbox.addWidget(self.hatchHlamp, 5, 1)
        gbox.addWidget(self.hatchHlabel, 5, 2)
        gbox.addWidget(self.hatchHExportBtn, 5, 3)

        #add nippersN
        gbox.addWidget(self.nippersNlamp, 6, 1)
        gbox.addWidget(self.nippersNlabel, 6, 2)
        gbox.addWidget(self.nippersNExportBtn, 6, 3)

        #add weldingplate WP
        gbox.addWidget(self.weldingplateWPlamp, 7, 1)
        gbox.addWidget(self.weldingplateWPlabel, 7, 2)
        gbox.addWidget(self.weldingplateWPExportBtn, 7, 3)

        #add hammer P
        gbox.addWidget(self.hammerPlamp, 8, 1)
        gbox.addWidget(self.hammerPlabel, 8, 2)
        gbox.addWidget(self.hammerPExportBtn, 8, 3)

        #add screwPlamp
        gbox.addWidget(self.screwPlamp, 9, 1)
        gbox.addWidget(self.screwPlabel, 9, 2)
        gbox.addWidget(self.screwPExportBtn, 9, 3)

        #add weldingplatformWPMlamp
        gbox.addWidget(self.weldingplatformWPMlamp, 10, 1)
        gbox.addWidget(self.weldingplatformWPMlabel, 10, 2)
        gbox.addWidget(self.weldingplatformWPMExportBtn, 10, 3)

        #add weldingmachineWMlamp
        gbox.addWidget(self.weldingmachineWMlamp, 11, 1)
        gbox.addWidget(self.weldingmachineWMlabel, 11, 2)
        gbox.addWidget(self.weldingmachineWMExportBtn, 11, 3)

        #add paneltoolPlamp
        gbox.addWidget(self.paneltoolPlamp, 12, 1)
        gbox.addWidget(self.paneltoolPlabel, 12, 2)
        gbox.addWidget(self.paneltoolPExportBtn, 12, 3)

        #add beltB1lamp
        gbox.addWidget(self.beltB1lamp, 13, 1)
        gbox.addWidget(self.beltB1label, 13, 2)
        gbox.addWidget(self.beltB1ExportBtn, 13, 3)

        #add beltB2lamp
        gbox.addWidget(self.beltB2lamp, 14, 1)
        gbox.addWidget(self.beltB2label, 14, 2)
        gbox.addWidget(self.beltB2ExportBtn, 14, 3)


        vbox = QtGui.QVBoxLayout()
        vbox.addItem(gbox)
        vbox.addWidget(self.refreshBtn)
        vbox.addWidget(self.outLog)
        # -------------------------------------SIGNALS AND SLOTS -----------------------------
        self.refreshBtn.clicked.connect(self.refreshScene)
        self.orlanDExportBtn.clicked.connect(self.exportOrlanDSlot)
        self.orlanSExportBtn.clicked.connect(self.exportOrlanSSlot)
        self.anchorAExportBtn.clicked.connect(self.exportAnchorASlot)
        self.anchorA2ExportBtn.clicked.connect(self.exportAnchorA2Slot)

        self.cameraCExportBtn.clicked.connect(self.exportCameraCSlot)
        self.hatchHExportBtn.clicked.connect(self.exportHatchHSlot)
        self.nippersNExportBtn.clicked.connect(self.exportNippersNSlot)
        self.weldingplateWPExportBtn.clicked.connect(self.exportWeldingplateWPSlot)
        self.hammerPExportBtn.clicked.connect(self.exportHammerPSlot)
        self.screwPExportBtn.clicked.connect(self.exportScrewPSlot)

        self.weldingplatformWPMExportBtn.clicked.connect(self.exportWeldingPlatformWPMSlot)
        self.weldingmachineWMExportBtn.clicked.connect(self.exportWeldingmachineWMSlot)
        self.paneltoolPExportBtn.clicked.connect(self.exportPaneltoolPSlot)
        self.beltB1ExportBtn.clicked.connect(self.exportbeltB1Slot)
        self.beltB2ExportBtn.clicked.connect(self.exportbeltB2Slot)

        # -------------------------------------WINDOW SETUP-----------------------------
        self.setLayout(vbox)
        self.setWindowTitle('SALUT: ALEMBIC EXPORT')
        self.setGeometry(300, 300, 450, 950)
        self.show()

    def refreshScene(self):
        self.outLog.clear()
        self.orlanDExportBtn.setText('Export >>')
        self.orlanSExportBtn.setText('Export >>')
        self.anchorAExportBtn.setText('Export >>')
        self.anchorA2ExportBtn.setText('Export >>')
        self.cameraCExportBtn.setText('Export >>')
        self.hatchHExportBtn.setText('Export >>')
        self.nippersNExportBtn.setText('Export >>')
        self.weldingplateWPExportBtn.setText('Export >>')
        self.hammerPExportBtn.setText('Export >>')
        self.screwPExportBtn.setText('Export >>')
        self.weldingplatformWPMExportBtn.setText('Export >>')
        self.weldingmachineWMExportBtn.setText('Export >>')
        self.paneltoolPExportBtn.setText('Export >>')
        self.beltB1ExportBtn.setText('Export >>')
        self.beltB2ExportBtn.setText('Export >>')
        # check if Maya Scene named correctly
        checkScene = getShotName()
        if ("ERROR" in checkScene):
            self.outLog.append(checkScene)
            return

        # refresh ORLAN D data
        count = 0
        for obj in self.orlanBaseGeoList:
            tmpObj = "D:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.orlanDlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.orlanDExportBtn.setEnabled(True)
        else:
            self.orlanDlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.orlanDExportBtn.setEnabled(False)
            self.outLog.append('ORLAN D is not found (check namespace - it should be D)')

        # refresh ORLAN S data
        count = 0
        for obj in self.orlanBaseGeoList:
            tmpObj = "S:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count >3):
            self.orlanSlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.orlanSExportBtn.setEnabled(True)
        else:
            self.orlanSlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.orlanSExportBtn.setEnabled(False)
            self.outLog.append('ORLAN S is not found (check namespace - it should be S)')

        # refresh anchor A data
        count = 0
        for obj in self.anchorBaseList:
            tmpObj = "A:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.anchorAlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.anchorAExportBtn.setEnabled(True)
        else:
            self.anchorAlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.anchorAExportBtn.setEnabled(False)
            self.outLog.append('ANCHOR A is not found (check namespace - it should be A)')

        # refresh anchor A2 data
        count = 0
        for obj in self.anchorBaseList:
            tmpObj = "A2:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.anchorA2lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.anchorA2ExportBtn.setEnabled(True)
        else:
            self.anchorA2lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.anchorA2ExportBtn.setEnabled(False)
            self.outLog.append('ANCHOR A2 is not found (check namespace - it should be A2)')

        # refresh camera C data
        count = 0
        for obj in self.cameraBaseList:
            tmpObj = "C:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.cameraClamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.cameraCExportBtn.setEnabled(True)
        else:
            self.cameraClamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.cameraCExportBtn.setEnabled(False)
            self.outLog.append('CAMERA C is not found (check namespace - it should be C)')

        # refresh hatch H data
        count = 0
        for obj in self.hatchBaseList:
            tmpObj = "H:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.hatchHlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.hatchHExportBtn.setEnabled(True)
        else:
            self.hatchHlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.hatchHExportBtn.setEnabled(False)
            self.outLog.append('HATCH H is not found (check namespace - it should be H)')

        # refresh NIPPERS N  data
        count = 0
        for obj in self.nippersBaseList:
            tmpObj = "N:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.nippersNlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.nippersNExportBtn.setEnabled(True)
        else:
            self.nippersNlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.nippersNExportBtn.setEnabled(False)
            self.outLog.append('NIPPERS N is not found (check namespace - it should be N)')

        # refresh WELDINGPLATE WP  data
        count = 0
        for obj in self.weldingplateBaseList:
            tmpObj = "WP:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.weldingplateWPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.weldingplateWPExportBtn.setEnabled(True)
        else:
            self.weldingplateWPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.weldingplateWPExportBtn.setEnabled(False)
            self.outLog.append('WELDING_PLATE WP is not found (check namespace - it should be WP)')

        # refresh hammer P data
        count = 0
        for obj in self.hammerBaseList:
            tmpObj = "P:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 0):
            self.hammerPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.hammerPExportBtn.setEnabled(True)
        else:
            self.hammerPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.hammerPExportBtn.setEnabled(False)
            self.outLog.append('HAMMER P is not found (check paneltool namespace - it should be P)')

        # refresh screw P  data
        count = 0
        for obj in self.screwdriverBaseList:
            tmpObj = "P:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.screwPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.screwPExportBtn.setEnabled(True)
        else:
            self.screwPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.screwPExportBtn.setEnabled(False)
            self.outLog.append('SCREWDRIVER P is not found (check paneltool namespace - it should be P)')

        # refresh welding platform WPM  data
        count = 0
        for obj in self.weldingplatformBaseList:
            tmpObj = "WPM:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.weldingplatformWPMlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.weldingplatformWPMExportBtn.setEnabled(True)
        else:
            self.weldingplatformWPMlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.weldingplatformWPMExportBtn.setEnabled(False)
            self.outLog.append('WELDING_PLATFORM WPM is not found (check namespace - it should be WPM)')

        # refresh weldingmachine WM data
        count = 0
        for obj in self.weldingmachineBaseList:
            tmpObj = "WM:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.weldingmachineWMlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.weldingmachineWMExportBtn.setEnabled(True)
        else:
            self.weldingmachineWMlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.weldingmachineWMExportBtn.setEnabled(False)
            self.outLog.append('WELDING_MACHINE WM is not found (check namespace - it should be WM)')

        # refresh paneltool P data
        count = 0
        for obj in self.weldingmachineBaseList:
            tmpObj = "P:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.paneltoolPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.paneltoolPExportBtn.setEnabled(True)
        else:
            self.paneltoolPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.paneltoolPExportBtn.setEnabled(False)
            self.outLog.append('PANEL_TOOL P is not found (check namespace - it should be WM)')

        # refresh belt B1 data
        count = 0
        for obj in self.beltBaseList:
            tmpObj = "B1:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.beltB1lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.beltB1ExportBtn.setEnabled(True)
        else:
            self.beltB1lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.beltB1ExportBtn.setEnabled(False)
            self.outLog.append('BELT B1 is not found (check namespace - it should be B1)')

        # refresh belt B1 data
        count = 0
        for obj in self.beltBaseList:
            tmpObj = "B1:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.beltB1lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.beltB1ExportBtn.setEnabled(True)
        else:
            self.beltB1lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.beltB1ExportBtn.setEnabled(False)
            self.outLog.append('BELT B1 is not found (check namespace - it should be B1)')

        # refresh belt B2 data
        count = 0
        for obj in self.beltBaseList:
            tmpObj = "B2:" + obj
            if cmds.objExists(tmpObj):
                count = count + 1
        if (count > 3):
            self.beltB2lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/GREEN_light.png'))
            self.beltB2ExportBtn.setEnabled(True)
        else:
            self.beltB2lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/RED_light.png'))
            self.beltB2ExportBtn.setEnabled(False)
            self.outLog.append('BELT B2 is not found (check namespace - it should be B2)')


    def exportOrlanDSlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_ORLAN-D_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        print fileName
                        abcver = fileName.split('.')[0][32:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)

        print ver

        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.orlanBaseGeoList:
            tmpObj = 'D:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.orlanDlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.orlanDExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('ORLAN D is exported to: \n"' + finalCachePath + '"\n')

    def exportOrlanSSlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_ORLAN-S_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][32:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.orlanBaseGeoList:
            tmpObj = 'S:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.orlanSlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.orlanSExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('ORLAN S is exported to: \n"' + finalCachePath + '"\n')


    def exportAnchorASlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_ANCHOR-A_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][33:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.anchorBaseList:
            tmpObj = 'A:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.anchorAlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.anchorAExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('ANCHOR A is exported to: \n"' + finalCachePath + '"\n')

    def exportAnchorA2Slot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_ANCHOR-A2_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][33:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.anchorBaseList:
            tmpObj = 'A2:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.anchorAlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.anchorAExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('ANCHOR A2 is exported to: \n"' + finalCachePath + '"\n')

    def exportCameraCSlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_CAMERA-C_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][33:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.cameraBaseList:
            tmpObj = 'C:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.cameraClamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.cameraCExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('CAMERA C is exported to: \n"' + finalCachePath + '"\n')

    def exportHatchHSlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_HATCH-H_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][32:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.hatchBaseList:
            tmpObj = 'H:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.hatchHlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.hatchHExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('HATCH H is exported to: \n"' + finalCachePath + '"\n')


    def exportNippersNSlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_NIPPERS-N_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][34:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.nippersBaseList:
            tmpObj = 'N:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.nippersNlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.nippersNExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('NIPPERS N is exported to: \n"' + finalCachePath + '"\n')


    def exportWeldingplateWPSlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_WELDINGPLATE-WP_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][40:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.weldingplateBaseList:
            tmpObj = 'WP:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.weldingplateWPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.weldingplateWPExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('WELDING_PLATE WP is exported to: \n"' + finalCachePath + '"\n')

    def exportHammerPSlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_HAMMER-P_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][33:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.hammerBaseList:
            tmpObj = 'P:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.hammerPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.hammerPExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('HAMMER P is exported to: \n"' + finalCachePath + '"\n')

    def exportScrewPSlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_SCREWDRIVER-P_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][38:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.screwdriverBaseList:
            tmpObj = 'P:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.screwPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.screwPExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('SCREWDRIVER P is exported to: \n"' + finalCachePath + '"\n')

    def exportWeldingPlatformWPMSlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_WELDING-PLATFORM-WPM_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][45:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.weldingplatformBaseList:
            tmpObj = 'WPM:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.weldingplatformWPMlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.weldingplatformWPMExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('WELDING_PLATFORM WPM is exported to: \n"' + finalCachePath + '"\n')

    def exportWeldingmachineWMSlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_WELDING-MACHINE-WM_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][43:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)

        #Generate list of full paths to groups
        fullGroupPaths = []
        for gr in  self.weldingMachineGroupsBaseList:
            namePlusNamespace = 'WM:' + gr
            cmds.select(namePlusNamespace, r=True)
            fullGroupPaths.append(cmds.ls(sl=True, l=True)[0])

        #select objects to export
        #generate list of shapes to select

        shapesToSelect = []

        for obj in self.weldingmachineBaseList:
            tmpObj = 'WM:' + obj
            tmpShape = cmds.listRelatives(tmpObj, s=True)[0]
            shapesToSelect.append(tmpShape)

        #clear current selection
        cmds.select(cl=True)

        #select all shapes
        for sh in shapesToSelect:
            cmds.select(sh, add=True)


        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws -sl '
        for obj in fullGroupPaths:
            objpath = '-root ' + obj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.weldingmachineWMlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.weldingmachineWMExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('WELDING_MACHINE WM is exported to: \n"' + finalCachePath + '"\n')
        # clear current selection
        cmds.select(cl=True)

    def exportPaneltoolPSlot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_PANELTOOL-P_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][36:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.paneltoolBaseList:
            tmpObj = 'P:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.paneltoolPlamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.paneltoolPExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('PANELTOOL P is exported to: \n"' + finalCachePath + '"\n')


    def exportbeltB1Slot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_BELT1-B1_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][33:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.beltBaseList:
            tmpObj = 'B1:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.beltB1lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.beltB1ExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('BELT1 B1 is exported to: \n"' + finalCachePath + '"\n')

    def exportbeltB2Slot(self):
        # Get Scene and Shot Names
        shotName = getShotName()
        sceneName = shotName[:3]
        # Get first and Last Frames
        timerange = getTimeRange()
        # Generate cache base name
        cacheBaseName = shotName + "_BELT2-B2_animation_v"
        # Generate Full Path to export caches
        fullABCStorePath = os.path.join(self.baseCachePath, sceneName, shotName)
        # Check if this folder exists
        folderExists = os.path.isdir(fullABCStorePath)
        if not folderExists:
            os.makedirs(fullABCStorePath)
        else:
            print "path " + fullABCStorePath + " already exists"

        # get list of all files in that folder
        fileList = os.listdir(fullABCStorePath)
        # check if chache files with same base name exists

        # CHECK CREATION TIME TO SHOW ORANGE LAMP IF CACHE HAS BEEN EXPORTED LESS THAN 15 MINUTES AGO

        # if it doesn't version == 01
        # if it does get version and add 1
        version = 1
        ver = ''
        if (len(fileList) > 0):
            for fileName in fileList:
                print fileName
                if ('.abc' in fileName):
                    if (cacheBaseName in fileName):
                        # get version
                        abcver = fileName.split('.')[0][33:]
                        if (int(abcver) >= version):
                            oldVersion = int(abcver)
                            version = oldVersion + 1

        # convert version to padded string and complete out abc name
        if (version < 10):
            ver = "0" + str(version)
        else:
            ver = str(version)
        print ver
        finalCacheName = cacheBaseName + ver + '.abc'
        finalCachePath = os.path.join(fullABCStorePath, finalCacheName)
        # Generate Alembic Export Command
        # select objects to export
        abcExportCommand = 'AbcExport -j "-frameRange ' + str(timerange[0]) + ' ' + str(
            timerange[1]) + ' -sn -ef -nn -uv -wfs -ws '
        for obj in self.beltBaseList:
            tmpObj = 'B2:' + obj
            objpath = '-root ' + tmpObj + ' '
            abcExportCommand = abcExportCommand + objpath
        abcExportCommand = abcExportCommand + ('-file ' + finalCachePath + '";')
        # Export Alembic
        import maya.mel as mel
        mel.eval(abcExportCommand)
        # Enable Orange Lamp
        self.beltB1lamp.setPixmap(QtGui.QPixmap('/prefs/maya/icons/ORANGE_light.png'))
        # Change Export Button text to exported
        self.beltB1ExportBtn.setText('Exported ||')
        # out Log result path
        self.outLog.append('BELT1 B2 is exported to: \n"' + finalCachePath + '"\n')