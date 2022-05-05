from asyncio.windows_events import NULL
from turtle import pu
import requests
import json
RO = {
 "@graph": [
    {
      "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190",
      "@type": "Person",
      "name": "Reem Wael"
    },
    {
      "@id": "9a4e89e1-13bf-4d44-b5f7-ced40eb33cb2",
      "@type": "Person",
      "name": "Constanza Figueroa"
    },
    {
      "@id": "data/Data Management Planning",
      "@type": "Dataset",
      "contactPoint": "Cameron Neylon",
      "path": "data/Data Management Planning",
      "description": "Collection of files relating to the Pilot Project Data Management Planning process. Includes 1) Data Inventories collected at the first workshop or soon after where data expected to be generated from contributing projects was enumerated 2) Data Management Plans prepared during the course of the project (see also the published DMPs in RIO journal for the finalised version) 3) Notes of interviews with the contributing projects about their experience of the DMP process and 4) A self audit of data sharing against what was proposed in the Data Management Plans.",
      "hasPart": [
        {
          "@id": "data/Data Management Planning/Data_Inventories"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Interviews"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Plans"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit"
        },
        {
          "@id": "data/Data Management Planning/Interim_Report_and_Comments"
        }
      ],
      "identifier": "./Data Management Planning",
      "name": "Data Management Planning"
    },
    {
      "@id": "data/Data Management Planning/Data_Inventories",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/Data Management Planning/Data_Inventories",
      "description": "Each contributing project prepared a \"Data Inventory\" as part of the initial workshop. This involved a template for enumerating data products from the contributing project, potential issues with sharing and important characteristics of the data outputs.",
      "hasPart": [
        {
          "@id": "data/Data Management Planning/Data_Inventories/BVH_107650_Virtual_Herbarium_CRIA_Data_inventory.xlsx"
        },
        {
          "@id": "data/Data Management Planning/Data_Inventories/DED_107771 - Copyright User Rights - Data Inventory.xlsx"
        },
        {
          "@id": "data/Data Management Planning/Data_Inventories/ECV_Data Audit Form-VN.xlsx"
        },
        {
          "@id": "data/Data Management Planning/Data_Inventories/IKC_107650_NaturalJustice_Data Inventory.xlsx"
        },
        {
          "@id": "data/Data Management Planning/Data_Inventories/NDF_20160401_Problemes_negliges_systeme_sante_Afrique_Niger__data inventory_FR.doc"
        },
        {
          "@id": "data/Data Management Planning/Data_Inventories/TED_20160325-108098-africa-tobacco-data-inventory.xlsx"
        },
        {
          "@id": "data/Data Management Planning/Data_Inventories/TED_20160406-108098-africa-tobacco-data-inventory.xlsx"
        }
      ],
      "identifier": "./Data Management Planning/Data_Inventories",
      "name": "Data Inventories"
    },
    {
      "@id": "data/Data Management Planning/Data_Inventories/BVH_107650_Virtual_Herbarium_CRIA_Data_inventory.xlsx",
      "@type": "File",
      "contentSize": "13800",
      "path": "data/Data Management Planning/Data_Inventories/BVH_107650_Virtual_Herbarium_CRIA_Data_inventory.xlsx",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8615-6652"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8615-6652"
      },
      "description": "Data Inventory for the Brazilian Virtual Herbarium Project",
      "encodingFormat": "Microsoft Excel for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/214",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "BVH_107650_Virtual_Herbarium_CRIA_Data_inventory.xlsx"
    },
    {
      "@id": "data/Data Management Planning/Data_Inventories/DED_107771 - Copyright User Rights - Data Inventory.xlsx",
      "@type": "File",
      "contentSize": "4862",
      "path": "data/Data Management Planning/Data_Inventories/DED_107771 - Copyright User Rights - Data Inventory.xlsx",
      "copyrightHolder": {
        "@id": "d0924b9b-a9ec-4b7f-bc7a-6d2f0582b219"
      },
      "creator": "Constanza Figuero",
      "description": "Data Inventory for the Derechos Digitales project",
      "encodingFormat": "Microsoft Excel for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/214",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "DED_107771 - Copyright User Rights - Data Inventory.xlsx"
    },
    {
      "@id": "data/Data Management Planning/Data_Inventories/ECV_Data Audit Form-VN.xlsx",
      "@type": "File",
      "contentSize": "29768",
      "path": "data/Data Management Planning/Data_Inventories/ECV_Data Audit Form-VN.xlsx",
      "copyrightHolder": {
        "@id": "a9baaf6c-c315-427e-a9a2-3a9bc06d0605"
      },
      "creator": {
        "@id": "a9baaf6c-c315-427e-a9a2-3a9bc06d0605"
      },
      "description": "Data Inventory for the Economic Committee of Vietnam project",
      "encodingFormat": "Microsoft Excel for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/214",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "ECV_Data Audit Form-VN.xlsx"
    },
    {
      "@id": "data/Data Management Planning/Data_Inventories/IKC_107650_NaturalJustice_Data Inventory.xlsx",
      "@type": "File",
      "contentSize": "15518",
      "path": "data/Data Management Planning/Data_Inventories/IKC_107650_NaturalJustice_Data Inventory.xlsx",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "description": "Data Inventory for the Indigenous Knowledge, Natural Justice project",
      "encodingFormat": "Microsoft Excel for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/214",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "IKC_107650_NaturalJustice_Data Inventory.xlsx"
    },
    {
      "@id": "data/Data Management Planning/Data_Inventories/NDF_20160401_Problemes_negliges_systeme_sante_Afrique_Niger__data inventory_FR.doc",
      "@type": "File",
      "contentSize": "84992",
      "path": "data/Data Management Planning/Data_Inventories/NDF_20160401_Problemes_negliges_systeme_sante_Afrique_Niger__data inventory_FR.doc",
      "copyrightHolder": {
        "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
      },
      "creator": {
        "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
      },
      "description": "Data Inventory for the Neglected Health Issues in Niger project",
      "encodingFormat": "Microsoft Word Document",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/40",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "NDF_20160401_Problemes_negliges_systeme_sante_Afrique_Niger__data inventory_FR.doc"
    },
    {
      "@id": "data/Data Management Planning/Data_Inventories/TED_20160325-108098-africa-tobacco-data-inventory.xlsx",
      "@type": "File",
      "contentSize": "14086",
      "path": "data/Data Management Planning/Data_Inventories/TED_20160325-108098-africa-tobacco-data-inventory.xlsx",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "description": "Data Inventory for the Tobacco Economics Data project v1",
      "encodingFormat": "Microsoft Excel for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/214",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "TED_20160325-108098-africa-tobacco-data-inventory.xlsx"
    },
    {
      "@id": "data/Data Management Planning/Data_Inventories/TED_20160406-108098-africa-tobacco-data-inventory.xlsx",
      "@type": "File",
      "contentSize": "16887",
      "path": "data/Data Management Planning/Data_Inventories/TED_20160406-108098-africa-tobacco-data-inventory.xlsx",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "description": "Data Inventory for the Tobacco Economics Data project v2",
      "encodingFormat": "Microsoft Excel for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/214",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "TED_20160406-108098-africa-tobacco-data-inventory.xlsx"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Interviews",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/Data Management Planning/Data_Management_Interviews",
      "description": "Notes of interviews that were taken with contributing project representatives during or after the process of Data Management Planning. The interviews focussed on which aspects of the data planning processes were useful or not. The interview prompt is also included.",
      "hasPart": [
        {
          "@id": "data/Data Management Planning/Data_Management_Interviews/AAA_CN20160610_DiscussionPlan.rtf"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Interviews/BVH_CN20160609_Dora_Cahnos_Note_of_discussion.rtf"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Interviews/DED_CN20160609_DanaeTapia_Note_of_discussion.rtf"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Interviews/ECV_CN20160608-Le_Dung_Trang_Note_of_discussion.rtf"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Interviews/HMP_CN20160602_Reem_Wael_Note_of_discussion.rtf"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Interviews/IKC_CN20160608_Cath_Traynor_&_Laura_Foster_Note_of_discussion.rtf"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Interviews/NDF_CN20160610_AissaDiarra_Note_of_discussion.rtf"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Interviews/TED_CN20160602_Lynn_Woolfrey_Note_of_discussion.rtf"
        }
      ],
      "identifier": "./Data Management Planning/Data_Management_Interviews",
      "name": "Data management interviews"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Interviews/AAA_CN20160610_DiscussionPlan.rtf",
      "@type": "File",
      "contentSize": "70398",
      "path": "data/Data Management Planning/Data_Management_Interviews/AAA_CN20160610_DiscussionPlan.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Discussion plan and questions for the interviews",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Data_Management_Interviews/AAA_CN20160610_DiscussionPlan.rtf"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Interviews/BVH_CN20160609_Dora_Cahnos_Note_of_discussion.rtf",
      "@type": "File",
      "contentSize": "155543",
      "path": "data/Data Management Planning/Data_Management_Interviews/BVH_CN20160609_Dora_Cahnos_Note_of_discussion.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Note of interview with Dora Canhos, BVH project",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Data_Management_Interviews/BVH_CN20160609_Dora_Cahnos_Note_of_discussion.rtf"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Interviews/DED_CN20160609_DanaeTapia_Note_of_discussion.rtf",
      "@type": "File",
      "contentSize": "14656",
      "path": "data/Data Management Planning/Data_Management_Interviews/DED_CN20160609_DanaeTapia_Note_of_discussion.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Note of interview with Danae Tapia, DED project",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/50",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Data_Management_Interviews/DED_CN20160609_DanaeTapia_Note_of_discussion.rtf"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Interviews/ECV_CN20160608-Le_Dung_Trang_Note_of_discussion.rtf",
      "@type": "File",
      "contentSize": "11919",
      "path": "data/Data Management Planning/Data_Management_Interviews/ECV_CN20160608-Le_Dung_Trang_Note_of_discussion.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Note of interview with Le Dang Trung, ECV project",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/50",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Data_Management_Interviews/ECV_CN20160608-Le_Dung_Trang_Note_of_discussion.rtf"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Interviews/HMP_CN20160602_Reem_Wael_Note_of_discussion.rtf",
      "@type": "File",
      "contentSize": "150840",
      "path": "data/Data Management Planning/Data_Management_Interviews/HMP_CN20160602_Reem_Wael_Note_of_discussion.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Note of interview with Reem Wael, HMP project",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Data_Management_Interviews/HMP_CN20160602_Reem_Wael_Note_of_discussion.rtf"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Interviews/IKC_CN20160608_Cath_Traynor_&_Laura_Foster_Note_of_discussion.rtf",
      "@type": "File",
      "contentSize": "216674",
      "path": "data/Data Management Planning/Data_Management_Interviews/IKC_CN20160608_Cath_Traynor_&_Laura_Foster_Note_of_discussion.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Note of interview with Cath Traynor, Laura Foster, IKC project",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Data_Management_Interviews/IKC_CN20160608_Cath_Traynor_&_Laura_Foster_Note_of_discussion.rtf"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Interviews/NDF_CN20160610_AissaDiarra_Note_of_discussion.rtf",
      "@type": "File",
      "contentSize": "170014",
      "path": "data/Data Management Planning/Data_Management_Interviews/NDF_CN20160610_AissaDiarra_Note_of_discussion.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Note of interview with Aïssa Diarra, NDF project and Pascal Aventurier, mentor and translator",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Data_Management_Interviews/NDF_CN20160610_AissaDiarra_Note_of_discussion.rtf"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Interviews/TED_CN20160602_Lynn_Woolfrey_Note_of_discussion.rtf",
      "@type": "File",
      "contentSize": "214894",
      "path": "data/Data Management Planning/Data_Management_Interviews/TED_CN20160602_Lynn_Woolfrey_Note_of_discussion.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Note of interview with Lynn Woolfrey, TED project",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Data_Management_Interviews/TED_CN20160602_Lynn_Woolfrey_Note_of_discussion.rtf"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Plans",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/Data Management Planning/Data_Management_Plans",
      "description": "As prepared and submitted versions of the Data Management Plans developed by the contributing projects as part of the pilot project. In some cases there are multiple versions available that allow progress to be examined over time. See also the finalised published Data Management Plans for some of the projects that are available through the collection at RIO journal.",
      "hasPart": [
        {
          "@id": "data/Data Management Planning/Data_Management_Plans/BVH_BVHDatavs2.docx"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Plans/DED_DMP-DerechosDigitales-DT.docx"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Plans/ECV_DMP Vietnam Project (1).docx"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Plans/HMP_DMP-harassmap-2016-06-02.pdf"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Plans/IKC_20161107_DMP_IKS & IPR Climate Change Project - Final.pdf"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Plans/IKC_IKS & IPR Climate Change Project-v1.pdf"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Plans/NDF_106949_Problemes_negliges_Niger_rdm-plan.doc"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Plans/NDF_20160504_PGD_Problemes_negliges_FR_Niger (3).doc"
        },
        {
          "@id": "data/Data Management Planning/Data_Management_Plans/TED_TobaccoEconomicData-20160429-project-108098-rdm-plan.pdf"
        }
      ],
      "identifier": "./Data Management Planning/Data_Management_Plans",
      "name": "Data Management Plans"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Plans/BVH_BVHDatavs2.docx",
      "@type": "File",
      "contentSize": "219888",
      "path": "data/Data Management Planning/Data_Management_Plans/BVH_BVHDatavs2.docx",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8615-6652"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8615-6652"
      },
      "description": "DMP from the BVH project",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "BVH_BVHDatavs2.docx",
      "sameAs": "https://doi.org/10.3897/rio.3.e14675"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Plans/DED_DMP-DerechosDigitales-DT.docx",
      "@type": "File",
      "contentSize": "86127",
      "path": "data/Data Management Planning/Data_Management_Plans/DED_DMP-DerechosDigitales-DT.docx",
      "copyrightHolder": {
        "@id": "d0924b9b-a9ec-4b7f-bc7a-6d2f0582b219"
      },
      "creator": {
        "@id": "d0924b9b-a9ec-4b7f-bc7a-6d2f0582b219"
      },
      "description": "DMP from the DED project",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "DED_DMP-DerechosDigitales-DT.docx"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Plans/ECV_DMP Vietnam Project (1).docx",
      "@type": "File",
      "contentSize": "138056",
      "path": "data/Data Management Planning/Data_Management_Plans/ECV_DMP Vietnam Project (1).docx",
      "copyrightHolder": {
        "@id": "a9baaf6c-c315-427e-a9a2-3a9bc06d0605"
      },
      "creator": {
        "@id": "a9baaf6c-c315-427e-a9a2-3a9bc06d0605"
      },
      "description": "DMP from the ECV project",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "ECV_DMP Vietnam Project (1).docx"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Plans/HMP_DMP-harassmap-2016-06-02.pdf",
      "@type": "File",
      "contentSize": "61069",
      "path": "data/Data Management Planning/Data_Management_Plans/HMP_DMP-harassmap-2016-06-02.pdf",
      "copyrightHolder": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "creator": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "description": "DMP from the HMP project",
      "encodingFormat": "Acrobat PDF 1.6 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/20",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "HMP_DMP-harassmap-2016-06-02.pdf",
      "sameAs": "https://doi.org/10.3897/rio.3.e15133"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Plans/IKC_20161107_DMP_IKS & IPR Climate Change Project - Final.pdf",
      "@type": "File",
      "contentSize": "258805",
      "path": "data/Data Management Planning/Data_Management_Plans/IKC_20161107_DMP_IKS & IPR Climate Change Project - Final.pdf",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "description": "DMP from the IKC project v2",
      "encodingFormat": "Acrobat PDF 1.3 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/17",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "IKC_20161107_DMP_IKS_IPR_Climate_Change_Project_-_Final.pdf",
      "sameAs": "https://doi.org/10.3897/rio.3.e15111"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Plans/IKC_IKS & IPR Climate Change Project-v1.pdf",
      "@type": "File",
      "contentSize": "84181",
      "path": "data/Data Management Planning/Data_Management_Plans/IKC_IKS & IPR Climate Change Project-v1.pdf",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "description": "DMP from the IKC project v1",
      "encodingFormat": "Acrobat PDF 1.4 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/18",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "IKC_IKS_IPR_Climate_Change_Project-v1.pdf"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Plans/NDF_106949_Problemes_negliges_Niger_rdm-plan.doc",
      "@type": "File",
      "contentSize": "79360",
      "path": "data/Data Management Planning/Data_Management_Plans/NDF_106949_Problemes_negliges_Niger_rdm-plan.doc",
      "copyrightHolder": [
        {
          "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
        },
        {
          "@id": "http://orcid.org/0000-0003-0211-4549"
        }
      ],
      "creator": [
        {
          "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
        },
        {
          "@id": "http://orcid.org/0000-0003-0211-4549"
        }
      ],
      "description": "DMP from the NDF project v1",
      "encodingFormat": "Microsoft Word Document",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/40",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "NDF_106949_Problemes_negliges_Niger_rdm-plan.doc"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Plans/NDF_20160504_PGD_Problemes_negliges_FR_Niger (3).doc",
      "@type": "File",
      "contentSize": "70144",
      "path": "data/Data Management Planning/Data_Management_Plans/NDF_20160504_PGD_Problemes_negliges_FR_Niger (3).doc",
      "copyrightHolder": [
        {
          "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
        },
        {
          "@id": "http://orcid.org/0000-0003-0211-4549"
        }
      ],
      "creator": [
        {
          "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
        },
        {
          "@id": "http://orcid.org/0000-0003-0211-4549"
        }
      ],
      "description": "DMP from the NDF project v2",
      "encodingFormat": "Microsoft Word Document",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/40",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "NDF_20160504_PGD_Problemes_negliges_FR_Niger_(3).doc"
    },
    {
      "@id": "data/Data Management Planning/Data_Management_Plans/TED_TobaccoEconomicData-20160429-project-108098-rdm-plan.pdf",
      "@type": "File",
      "contentSize": "54165",
      "path": "data/Data Management Planning/Data_Management_Plans/TED_TobaccoEconomicData-20160429-project-108098-rdm-plan.pdf",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "description": "DMP from the TED project",
      "encodingFormat": "Acrobat PDF 1.4 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/18",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "TED_TobaccoEconomicData-20160429-project-108098-rdm-plan.pdf",
      "sameAs": "https://doi.org/10.3897/rio.3.e14837"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/Data Management Planning/Final_Self_Audit",
      "description": "In the final project workshop the participating project were invited to conduct a self-audit of their performance against a summary of their Data Management Plan. The templates given to each project are in the directory \"Templates for Self Audit\" This directory contains either an image of the hand completed template or a digital file. For those with images a transcript is also provided. In the case of the NDF project the transcript is a translation of the original French.",
      "hasPart": [
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/DED_Constanza-Lunch_audit_transcript.pdf"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/DED_IMG_20161202_161808.jpg"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/ECV_Trung-Lunch_audit.docx"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/HMP_IMG_20161202_161825.jpg"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/HMP_Reem-Lunch_audit_transcript.pdf"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/IKC_Cath-Lunch_audit_transcript.pdf"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/IKC_IMG_20161202_161840.jpg"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/IKC_IMG_20161230_122053.jpg"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/NDF_Aissa-Lunch_audit_transcript.pdf"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/NDF_IMG_20161230_115536.jpg"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/TED_20161202-african-tobacco-data-lw.xlsx"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit"
        }
      ],
      "identifier": "./Data Management Planning/Final_Self_Audit",
      "name": "Final self audit"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/DED_Constanza-Lunch_audit_transcript.pdf",
      "@type": "File",
      "contentSize": "25474",
      "path": "data/Data Management Planning/Final_Self_Audit/DED_Constanza-Lunch_audit_transcript.pdf",
      "copyrightHolder": {
        "@id": "9a4e89e1-13bf-4d44-b5f7-ced40eb33cb2"
      },
      "creator": {
        "@id": "9a4e89e1-13bf-4d44-b5f7-ced40eb33cb2"
      },
      "description": "Trancribed version of the DED self audit",
      "encodingFormat": "Acrobat PDF 1.5 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/19",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Final_Self_Audit/DED_Constanza-Lunch_audit_transcript.pdf"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/DED_IMG_20161202_161808.jpg",
      "@type": "File",
      "contentSize": "1056032",
      "path": "data/Data Management Planning/Final_Self_Audit/DED_IMG_20161202_161808.jpg",
      "copyrightHolder": {
        "@id": "9a4e89e1-13bf-4d44-b5f7-ced40eb33cb2"
      },
      "creator": {
        "@id": "9a4e89e1-13bf-4d44-b5f7-ced40eb33cb2"
      },
      "description": "Image of the DED self audit",
      "encodingFormat": "JPEG File Interchange Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/43",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Final_Self_Audit/DED_IMG_20161202_161808.jpg"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/ECV_Trung-Lunch_audit.docx",
      "@type": "File",
      "contentSize": "109827",
      "path": "data/Data Management Planning/Final_Self_Audit/ECV_Trung-Lunch_audit.docx",
      "copyrightHolder": {
        "@id": "a9baaf6c-c315-427e-a9a2-3a9bc06d0605"
      },
      "creator": {
        "@id": "a9baaf6c-c315-427e-a9a2-3a9bc06d0605"
      },
      "description": "Digital version of the ECV self audit",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Final_Self_Audit/ECV_Trung-Lunch_audit.docx"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/HMP_IMG_20161202_161825.jpg",
      "@type": "File",
      "contentSize": "1187891",
      "path": "data/Data Management Planning/Final_Self_Audit/HMP_IMG_20161202_161825.jpg",
      "copyrightHolder": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "creator": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "description": "Image of the HMP self audit",
      "encodingFormat": "JPEG File Interchange Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/43",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Final_Self_Audit/HMP_IMG_20161202_161825.jpg"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/HMP_Reem-Lunch_audit_transcript.pdf",
      "@type": "File",
      "contentSize": "22944",
      "path": "data/Data Management Planning/Final_Self_Audit/HMP_Reem-Lunch_audit_transcript.pdf",
      "copyrightHolder": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "creator": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "description": "Trancribed version of the HMP self audit",
      "encodingFormat": "Acrobat PDF 1.5 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/19",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Final_Self_Audit/HMP_Reem-Lunch_audit_transcript.pdf"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/IKC_Cath-Lunch_audit_transcript.pdf",
      "@type": "File",
      "contentSize": "40860",
      "path": "data/Data Management Planning/Final_Self_Audit/IKC_Cath-Lunch_audit_transcript.pdf",
      "copyrightHolder": [
        {
          "@id": "http://orcid.org/0000-0002-9661-487X"
        },
        {
          "@id": "b9947255-54a2-4120-8845-faecf37ae2e8"
        }
      ],
      "creator": [
        {
          "@id": "http://orcid.org/0000-0002-9661-487X"
        },
        {
          "@id": "b9947255-54a2-4120-8845-faecf37ae2e8"
        }
      ],
      "description": "Trancribed version of the IKC self audit",
      "encodingFormat": "Acrobat PDF 1.5 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/19",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Final_Self_Audit/IKC_Cath-Lunch_audit_transcript.pdf"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/IKC_IMG_20161202_161840.jpg",
      "@type": "File",
      "contentSize": "1258329",
      "path": "data/Data Management Planning/Final_Self_Audit/IKC_IMG_20161202_161840.jpg",
      "copyrightHolder": [
        {
          "@id": "http://orcid.org/0000-0002-9661-487X"
        },
        {
          "@id": "b9947255-54a2-4120-8845-faecf37ae2e8"
        }
      ],
      "creator": [
        {
          "@id": "http://orcid.org/0000-0002-9661-487X"
        },
        {
          "@id": "b9947255-54a2-4120-8845-faecf37ae2e8"
        }
      ],
      "description": "Image of the IKC self audit part 1",
      "encodingFormat": "JPEG File Interchange Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/43",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Final_Self_Audit/IKC_IMG_20161202_161840.jpg"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/IKC_IMG_20161230_122053.jpg",
      "@type": "File",
      "contentSize": "2757978",
      "path": "data/Data Management Planning/Final_Self_Audit/IKC_IMG_20161230_122053.jpg",
      "copyrightHolder": [
        {
          "@id": "http://orcid.org/0000-0002-9661-487X"
        },
        {
          "@id": "b9947255-54a2-4120-8845-faecf37ae2e8"
        }
      ],
      "creator": [
        {
          "@id": "http://orcid.org/0000-0002-9661-487X"
        },
        {
          "@id": "b9947255-54a2-4120-8845-faecf37ae2e8"
        }
      ],
      "description": "Image of the IKC self audit part 2",
      "encodingFormat": "Exchangeable Image File Format (Compressed)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/x-fmt/391",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Final_Self_Audit/IKC_IMG_20161230_122053.jpg"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/NDF_Aissa-Lunch_audit_transcript.pdf",
      "@type": "File",
      "contentSize": "43726",
      "path": "data/Data Management Planning/Final_Self_Audit/NDF_Aissa-Lunch_audit_transcript.pdf",
      "copyrightHolder": {
        "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
      },
      "creator": {
        "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
      },
      "description": "Transcribed version of the NDF self audit",
      "encodingFormat": "Acrobat PDF 1.5 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/19",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Final_Self_Audit/NDF_Aissa-Lunch_audit_transcript.pdf"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/NDF_IMG_20161230_115536.jpg",
      "@type": "File",
      "contentSize": "3835579",
      "path": "data/Data Management Planning/Final_Self_Audit/NDF_IMG_20161230_115536.jpg",
      "copyrightHolder": {
        "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
      },
      "creator": {
        "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
      },
      "description": "Image of the NDF self audit",
      "encodingFormat": "Exchangeable Image File Format (Compressed)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/x-fmt/391",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Final_Self_Audit/NDF_IMG_20161230_115536.jpg"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/TED_20161202-african-tobacco-data-lw.xlsx",
      "@type": "File",
      "contentSize": "12477",
      "path": "data/Data Management Planning/Final_Self_Audit/TED_20161202-african-tobacco-data-lw.xlsx",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "description": "Digital version of the TED self audit",
      "encodingFormat": "Microsoft Excel for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/214",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Data Management Planning/Final_Self_Audit/TED_20161202-african-tobacco-data-lw.xlsx"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit",
      "description": "The digital version of the documents given to participants in the final workshop to audit their performance against the Data Management Plans that they had previously prepared.",
      "hasPart": [
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_DED_self_audit.docx"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_ECV_self_audit.docx"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_HMP_self_audit.docx"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_IKC_self_audit.docx"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_NDF_self_audit.docx"
        },
        {
          "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_TED_self_audit.docx"
        }
      ],
      "identifier": "./Data Management Planning/Final_Self_Audit/Templates_for_self_audit",
      "name": "Templates for Self Audit"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_DED_self_audit.docx",
      "@type": "File",
      "contentSize": "70930",
      "path": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_DED_self_audit.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Empty template for data audit for DED project",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "AAA_Template_DED_self_audit.docx"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_ECV_self_audit.docx",
      "@type": "File",
      "contentSize": "75046",
      "path": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_ECV_self_audit.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Empty template for data audit for ECV project",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "AAA_Template_ECV_self_audit.docx"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_HMP_self_audit.docx",
      "@type": "File",
      "contentSize": "69075",
      "path": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_HMP_self_audit.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Empty template for data audit for HMP project",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "AAA_Template_HMP_self_audit.docx"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_IKC_self_audit.docx",
      "@type": "File",
      "contentSize": "75635",
      "path": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_IKC_self_audit.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Empty template for data audit for IKC project",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "AAA_Template_IKC_self_audit.docx"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_NDF_self_audit.docx",
      "@type": "File",
      "contentSize": "78214",
      "path": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_NDF_self_audit.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Empty template for data audit for NDF project",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "AAA_Template_NDF_self_audit.docx"
    },
    {
      "@id": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_TED_self_audit.docx",
      "@type": "File",
      "contentSize": "73224",
      "path": "data/Data Management Planning/Final_Self_Audit/Templates_for_self_audit/AAA_Template_TED_self_audit.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Empty template for data audit for TED project",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "AAA_Template_TED_self_audit.docx"
    },
    {
      "@id": "data/Data Management Planning/Interim_Report_and_Comments",
      "@type": "Dataset",
      "contactPoint": " Cameron Neylon",
      "path": "data/Data Management Planning/Interim_Report_and_Comments",
      "description": "During the pilot an Interim Report was prepared and used the prompt reponses both from staff within IDRC and from the participating project. This directory contains both the interim report and the responses in varios forms. These include responses as written text documents or appended to the report (BVH, IKC projects and NDF project in French), comments on the original word document of the interim report (IDRC itself, TED).",
      "hasPart": [
        {
          "@id": "data/Data Management Planning/Interim_Report_and_Comments/AAA_Data_Audits_and_DMPs_ Interim Report.pdf"
        },
        {
          "@id": "data/Data Management Planning/Interim_Report_and_Comments/BVH_Virtual_Herbarium_-_Dora_Canhos.pdf"
        },
        {
          "@id": "data/Data Management Planning/Interim_Report_and_Comments/IDRC_DataAuditsandDMPsInterimReport-comments.docx"
        },
        {
          "@id": "data/Data Management Planning/Interim_Report_and_Comments/IDRC_DataAuditsandDMPsInterimReport-comments.pdf"
        },
        {
          "@id": "data/Data Management Planning/Interim_Report_and_Comments/IKC_Commentary-DMPs - Cath (IPs and IKS).pdf"
        },
        {
          "@id": "data/Data Management Planning/Interim_Report_and_Comments/NDF_WorkOpenDatas_LASDEL_Niger_20161127.doc"
        },
        {
          "@id": "data/Data Management Planning/Interim_Report_and_Comments/NDF_WorkOpenDatas_LASDEL_Niger_20161127.pdf"
        },
        {
          "@id": "data/Data Management Planning/Interim_Report_and_Comments/TED_20161025-DataAudistandDMPsInterimReport-lw.pdf"
        },
        {
          "@id": "data/Data Management Planning/Interim_Report_and_Comments/TED_20161025-DataAuditsandDMPsInterimReport-lw.docx"
        }
      ],
      "identifier": "./Data Management Planning/Interim_Report_and_Comments",
      "name": "Interim Report and Comments"
    },
    {
      "@id": "data/Data Management Planning/Interim_Report_and_Comments/AAA_Data_Audits_and_DMPs_ Interim Report.pdf",
      "@type": "File",
      "contentSize": "288599",
      "path": "data/Data Management Planning/Interim_Report_and_Comments/AAA_Data_Audits_and_DMPs_ Interim Report.pdf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "The interim report prepared during the project following the DMP interviews but before all the DMPs were completed. Notes progress and initial findings.",
      "encodingFormat": "Acrobat PDF 1.5 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/19",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "AAA_Data_Audits_and_DMPs_ Interim Report.pdf"
    },
    {
      "@id": "data/Data Management Planning/Interim_Report_and_Comments/BVH_Virtual_Herbarium_-_Dora_Canhos.pdf",
      "@type": "File",
      "contentSize": "86161",
      "path": "data/Data Management Planning/Interim_Report_and_Comments/BVH_Virtual_Herbarium_-_Dora_Canhos.pdf",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8615-6652"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8615-6652"
      },
      "description": "Response to the interim report from BVH project",
      "encodingFormat": "Acrobat PDF 1.5 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/19",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "BVH_Virtual_Herbarium_-_Dora_Canhos.pdf"
    },
    {
      "@id": "data/Data Management Planning/Interim_Report_and_Comments/IDRC_DataAuditsandDMPsInterimReport-comments.docx",
      "@type": "File",
      "contentSize": "37429",
      "path": "data/Data Management Planning/Interim_Report_and_Comments/IDRC_DataAuditsandDMPsInterimReport-comments.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "IDRC"
      },
      "description": "Reponse to the interim report from the IDRC team (comments on word doc)",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "IDRC_DataAuditsandDMPsInterimReport-comments.docx"
    },
    {
      "@id": "data/Data Management Planning/Interim_Report_and_Comments/IDRC_DataAuditsandDMPsInterimReport-comments.pdf",
      "@type": "File",
      "contentSize": "70710",
      "path": "data/Data Management Planning/Interim_Report_and_Comments/IDRC_DataAuditsandDMPsInterimReport-comments.pdf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "IDRC"
      },
      "description": "Reponse to the interim report from the IDRC team (pdf version)",
      "encodingFormat": "Acrobat PDF 1.3 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/17",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "IDRC_DataAuditsandDMPsInterimReport-comments.pdf"
    },
    {
      "@id": "data/Data Management Planning/Interim_Report_and_Comments/IKC_Commentary-DMPs - Cath (IPs and IKS).pdf",
      "@type": "File",
      "contentSize": "292685",
      "path": "data/Data Management Planning/Interim_Report_and_Comments/IKC_Commentary-DMPs - Cath (IPs and IKS).pdf",
      "copyrightHolder": "Cath Traynor, Laura Foster",
      "creator": [
        {
          "@id": "http://orcid.org/0000-0002-9661-487X"
        },
        {
          "@id": "b9947255-54a2-4120-8845-faecf37ae2e8"
        }
      ],
      "description": "Response to the interim report from IKC project",
      "encodingFormat": "Acrobat PDF/A - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/95",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "IKC_Commentary-DMPs - Cath (IPs and IKS).pdf"
    },
    {
      "@id": "data/Data Management Planning/Interim_Report_and_Comments/NDF_WorkOpenDatas_LASDEL_Niger_20161127.doc",
      "@type": "File",
      "contentSize": "64000",
      "path": "data/Data Management Planning/Interim_Report_and_Comments/NDF_WorkOpenDatas_LASDEL_Niger_20161127.doc",
      "copyrightHolder": "Aïssa Diarra, Pascal Aventurier",
      "creator": [
        {
          "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
        },
        {
          "@id": "http://orcid.org/0000-0003-0211-4549"
        }
      ],
      "description": "Response to the interim report from NDF project (addendum to word document)",
      "encodingFormat": "Microsoft Word Document",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/40",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "NDF_WorkOpenDatas_LASDEL_Niger_20161127.doc"
    },
    {
      "@id": "data/Data Management Planning/Interim_Report_and_Comments/NDF_WorkOpenDatas_LASDEL_Niger_20161127.pdf",
      "@type": "File",
      "contentSize": "111219",
      "path": "data/Data Management Planning/Interim_Report_and_Comments/NDF_WorkOpenDatas_LASDEL_Niger_20161127.pdf",
      "copyrightHolder": "Aïssa Diarra, Pascal Aventurier",
      "creator": [
        {
          "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
        },
        {
          "@id": "http://orcid.org/0000-0003-0211-4549"
        }
      ],
      "description": "Response to the interim report from NDF project (pdf version)",
      "encodingFormat": "Acrobat PDF 1.3 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/17",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "NDF_WorkOpenDatas_LASDEL_Niger_20161127.pdf"
    },
    {
      "@id": "data/Data Management Planning/Interim_Report_and_Comments/TED_20161025-DataAudistandDMPsInterimReport-lw.pdf",
      "@type": "File",
      "contentSize": "374072",
      "path": "data/Data Management Planning/Interim_Report_and_Comments/TED_20161025-DataAudistandDMPsInterimReport-lw.pdf",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "description": "Response to the interim report from TED project (addendum to word document)",
      "encodingFormat": "Acrobat PDF 1.3 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/17",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "TED_20161025-DataAudistandDMPsInterimReport-lw.pdf"
    },
    {
      "@id": "data/Data Management Planning/Interim_Report_and_Comments/TED_20161025-DataAuditsandDMPsInterimReport-lw.docx",
      "@type": "File",
      "contentSize": "312151",
      "path": "data/Data Management Planning/Interim_Report_and_Comments/TED_20161025-DataAuditsandDMPsInterimReport-lw.docx",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "description": "Response to the interim report from TED project (pdf version)",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "TED_20161025-DataAuditsandDMPsInterimReport-lw.docx"
    },
    {
      "@id": "DenverSheraton",
      "@type": "Place",
      "URL": "http://www.sheratondenverdowntown.com/?SWAQ=958P",
      "address": "1550 Court Pl, Denver, CO 80202, USA",
      "description": "The location of the 2016 SciDataCon meeting and associated data-related meetings in Denver",
      "identifier": "DenverSheraton",
      "name": "Sheraton Denver Downtown Hotel"
    },
    {
      "@id": "data/Final_Project_Workshop_Materials",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/Final_Project_Workshop_Materials",
      "description": "The workshop booklets that were used to suppor the second of the two workshops undertaken as part of the workshop. Includes versions with advisor prompts and translations of both forms of the booklet into French.",
      "hasPart": [
        {
          "@id": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet.docx"
        },
        {
          "@id": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet_facilitator.docx"
        },
        {
          "@id": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet_facilitator_francais.docx"
        },
        {
          "@id": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet_francais.docx"
        }
      ],
      "identifier": "./Final_Project_Workshop_Materials",
      "name": "Final Workshop Materials"
    },
    {
      "@id": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet.docx",
      "@type": "File",
      "contentSize": "655774",
      "path": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "The participant booklet and agenda for the final workshop",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "FinalWorkshopBooklet.docx"
    },
    {
      "@id": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet_facilitator.docx",
      "@type": "File",
      "contentSize": "655719",
      "path": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet_facilitator.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "The facilitator booklet and agenda for the final workshop containing additional prompts and guidance for faciliatators and experts",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "FinalWorkshopBooklet_facilitator.docx"
    },
    {
      "@id": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet_facilitator_francais.docx",
      "@type": "File",
      "contentSize": "654794",
      "path": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet_facilitator_francais.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "The participant booklet and agenda for the final workshop translated into French",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "FinalWorkshopBooklet_facilitator_francais.docx"
    },
    {
      "@id": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet_francais.docx",
      "@type": "File",
      "contentSize": "657597",
      "path": "data/Final_Project_Workshop_Materials/FinalWorkshopBooklet_francais.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "The facilitator booklet and agenda for the final workshop containing additional prompts and guidance for faciliatators and experts, translated into French",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "FinalWorkshopBooklet_francais.docx"
    },
    {
      "@id": "data/Final_Project_Workshop_Presentations",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/Final_Project_Workshop_Presentations",
      "description": "The presentations given by the contributing projects at the final project workshop held in Ottawa in December 2016. Each presentation summarised experiences and challenges that the projects had experienced in implementing their Data Management Plans. Includes translations to or from French prepared for most of the participating project presentations.",
      "identifier": "./Final_Project_Workshop_Presentations",
      "name": "Final_Project_Workshop_Presentations",
      "title": "Final Workshop Presentations"
    },
    {
      "@id": "IDRC",
      "@type": "Organization",
      "address": "150 Kent Street, Ottawa, Ontario, Canada K1P 0B2",
      "description": "Canadian Frown Corporation and funder of development research",
      "identifier": "IDRC",
      "name": "International Development Research Center"
    },
    {
      "@id": "IDRCHQ",
      "@type": "Place",
      "URL": "https://www.idrc.ca/",
      "address": "150 Kent St, Ottawa, ON K1P 0B2, Canada",
      "description": "The Ottaw Headquarters of the IDRC",
      "identifier": "IDRCHQ",
      "name": "IDRC"
    },
    {
      "@id": "data/Introductory_Data_Workshop_Materials",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/Introductory_Data_Workshop_Materials",
      "description": "The first point of contact with the contributing projects was a workshop held at IDRC headquarters in Ottawa from March 7-10 2016. The workshop was supported by a booklet provided to workshop participants which is provided here in several different forms, the participant version, a version with notes for the advisors/mentors and the participant workbook translated into French.",
      "hasPart": [
        {
          "@id": "data/Introductory_Data_Workshop_Materials/WorkshopBookletAdvisorNotes.docx"
        },
        {
          "@id": "data/Introductory_Data_Workshop_Materials/WorkshopBookletFormatted.docx"
        },
        {
          "@id": "data/Introductory_Data_Workshop_Materials/WorkshopBookletParticipants.docx"
        },
        {
          "@id": "data/Introductory_Data_Workshop_Materials/WorkshopBookletParticipantsFrancais.docx"
        }
      ],
      "identifier": "./Introductory_Data_Workshop_Materials",
      "name": "Introductory Data Workshop Materials"
    },
    {
      "@id": "data/Introductory_Data_Workshop_Materials/WorkshopBookletAdvisorNotes.docx",
      "@type": "File",
      "contentSize": "1102820",
      "path": "data/Introductory_Data_Workshop_Materials/WorkshopBookletAdvisorNotes.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "The booklet for the introductory workshop including the notes for advisors.",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "WorkshopBookletAdvisorNotes.docx"
    },
    {
      "@id": "data/Introductory_Data_Workshop_Materials/WorkshopBookletFormatted.docx",
      "@type": "File",
      "contentSize": "1102002",
      "path": "data/Introductory_Data_Workshop_Materials/WorkshopBookletFormatted.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "The participant booklet from the workshop, including some notes taken during the conduct of the first workshop.",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "WorkshopBookletFormatted.docx"
    },
    {
      "@id": "data/Introductory_Data_Workshop_Materials/WorkshopBookletParticipants.docx",
      "@type": "File",
      "contentSize": "1091661",
      "path": "data/Introductory_Data_Workshop_Materials/WorkshopBookletParticipants.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "The participant booklet from the workshop.",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "WorkshopBookletParticipants.docx"
    },
    {
      "@id": "data/Introductory_Data_Workshop_Materials/WorkshopBookletParticipantsFrancais.docx",
      "@type": "File",
      "contentSize": "1093136",
      "path": "data/Introductory_Data_Workshop_Materials/WorkshopBookletParticipantsFrancais.docx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "The participant booklet from the workshop, translated into French.",
      "encodingFormat": "Microsoft Word for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/412",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "WorkshopBookletParticipantsFrancais.docx"
    },
    {
      "@id": "data/Introductory_Workshop_Presentations",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/Introductory_Workshop_Presentations",
      "description": "At the introductory workshop each participating project gave a presentation describing their background and project. ",
      "hasPart": [
        {
          "@id": "data/Introductory_Workshop_Presentations/BVH_8_OCSDNetDoraIDRC.pptx"
        },
        {
          "@id": "data/Introductory_Workshop_Presentations/DED_4_DanaeTapiaPresentation.pptx"
        },
        {
          "@id": "data/Introductory_Workshop_Presentations/ECV_3_Vietnam-IDRC Workshop.pptx"
        },
        {
          "@id": "data/Introductory_Workshop_Presentations/HMP_1_HarassMap. Ottawa.pptx"
        },
        {
          "@id": "data/Introductory_Workshop_Presentations/IKC_7_IDRC_DataSharing_NaturalJustice.pptx"
        },
        {
          "@id": "data/Introductory_Workshop_Presentations/NDF_6_LASDEL_PNSS_CRDI.ppt"
        },
        {
          "@id": "data/Introductory_Workshop_Presentations/TED_5_20160308-idrc-od-project-woolfrey.pptx"
        }
      ],
      "identifier": "./Introductory_Workshop_Presentations",
      "name": "Presentations given at the introductory workshop"
    },
    {
      "@id": "data/Introductory_Workshop_Presentations/BVH_8_OCSDNetDoraIDRC.pptx",
      "@type": "File",
      "contentSize": "3168683",
      "path": "data/Introductory_Workshop_Presentations/BVH_8_OCSDNetDoraIDRC.pptx",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8615-6652"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8615-6652"
      },
      "description": "Initial presentation to group from BVH project",
      "encodingFormat": "Microsoft Powerpoint for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/215",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Introductory_Workshop_Presentations/BVH_8_OCSDNetDoraIDRC.pptx"
    },
    {
      "@id": "data/Introductory_Workshop_Presentations/DED_4_DanaeTapiaPresentation.pptx",
      "@type": "File",
      "contentSize": "69695",
      "path": "data/Introductory_Workshop_Presentations/DED_4_DanaeTapiaPresentation.pptx",
      "copyrightHolder": {
        "@id": "d0924b9b-a9ec-4b7f-bc7a-6d2f0582b219"
      },
      "creator": {
        "@id": "d0924b9b-a9ec-4b7f-bc7a-6d2f0582b219"
      },
      "description": "Initial presentation to group from DED project",
      "encodingFormat": "Microsoft Powerpoint for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/215",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Introductory_Workshop_Presentations/DED_4_DanaeTapiaPresentation.pptx"
    },
    {
      "@id": "data/Introductory_Workshop_Presentations/ECV_3_Vietnam-IDRC Workshop.pptx",
      "@type": "File",
      "contentSize": "2221793",
      "path": "data/Introductory_Workshop_Presentations/ECV_3_Vietnam-IDRC Workshop.pptx",
      "copyrightHolder": {
        "@id": "a9baaf6c-c315-427e-a9a2-3a9bc06d0605"
      },
      "creator": {
        "@id": "a9baaf6c-c315-427e-a9a2-3a9bc06d0605"
      },
      "description": "Initial presentation to group from ECV project",
      "encodingFormat": "Microsoft Powerpoint for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/215",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Introductory_Workshop_Presentations/ECV_3_Vietnam-IDRC Workshop.pptx"
    },
    {
      "@id": "data/Introductory_Workshop_Presentations/HMP_1_HarassMap. Ottawa.pptx",
      "@type": "File",
      "contentSize": "515465",
      "path": "data/Introductory_Workshop_Presentations/HMP_1_HarassMap. Ottawa.pptx",
      "copyrightHolder": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "creator": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "description": "Initial presentation to group from JMP project",
      "encodingFormat": "Microsoft Powerpoint for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/215",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Introductory_Workshop_Presentations/HMP_1_HarassMap. Ottawa.pptx"
    },
    {
      "@id": "data/Introductory_Workshop_Presentations/IKC_7_IDRC_DataSharing_NaturalJustice.pptx",
      "@type": "File",
      "contentSize": "234088",
      "path": "data/Introductory_Workshop_Presentations/IKC_7_IDRC_DataSharing_NaturalJustice.pptx",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "description": "Initial presentation to group from IKC project",
      "encodingFormat": "Microsoft Powerpoint for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/215",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Introductory_Workshop_Presentations/IKC_7_IDRC_DataSharing_NaturalJustice.pptx"
    },
    {
      "@id": "data/Introductory_Workshop_Presentations/NDF_6_LASDEL_PNSS_CRDI.ppt",
      "@type": "File",
      "contentSize": "121856",
      "path": "data/Introductory_Workshop_Presentations/NDF_6_LASDEL_PNSS_CRDI.ppt",
      "copyrightHolder": {
        "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
      },
      "creator": {
        "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa"
      },
      "description": "Initial presentation to group from NDF project",
      "encodingFormat": "Microsoft Powerpoint Presentation",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/126",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Introductory_Workshop_Presentations/NDF_6_LASDEL_PNSS_CRDI.ppt"
    },
    {
      "@id": "data/Introductory_Workshop_Presentations/TED_5_20160308-idrc-od-project-woolfrey.pptx",
      "@type": "File",
      "contentSize": "688551",
      "path": "data/Introductory_Workshop_Presentations/TED_5_20160308-idrc-od-project-woolfrey.pptx",
      "copyrightHolder": "Lynn Wollfrey",
      "creator": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "description": "Initial presentation to group from TED project",
      "encodingFormat": "Microsoft Powerpoint for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/215",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Introductory_Workshop_Presentations/TED_5_20160308-idrc-od-project-woolfrey.pptx"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/Policy and Implementation Review Interviews",
      "description": "A review of Data Management Planning policy and implementation was comissioned as part of the project (https://doi.org/10.3897/rio.3.e14673). This included interviews with RDM experts on a range of policy and implementation issues. The associated questions were provided to interviewees in advance. Most interviews were conducted at the RDA plenary in Paris, 24-25 September 2015",
      "hasPart": [
        {
          "@id": "data/Policy and Implementation Review Interviews/RDAInterviewQuestions.pdf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes"
        }
      ],
      "identifier": "./Policy and Implementation Review Interviews",
      "name": "Policy and Implementation Review Interviews",
      "relatedLink": "https://doi.org/10.3897/rio.3.e14673",
      "title": "Data Management Planning Policy and Implementation Reviews"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio",
      "@type": "Dataset",
      "contactPoint": "Cameron Neylon",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio",
      "description": "For the initial review contributing to the project a series of interviews were conducted with relevant experts on data management and open data policy and implementation. These are the audio records of those interviews.",
      "hasPart": [
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-11_11-Anita_de_Waard.flac"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-11_11-Anita_de_Waard.wav"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_34-Michael_Ball.flac"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_34-Michael_Ball.wav"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_57-Carly_Strasser.flac"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_57-Carly_Strasser.wav"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-14_28-Patricia_Cruze.flac"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-14_28-Patricia_Cruze.wav"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-15_52-David_Carr.flac"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-15_52-David_Carr.wav"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_06-Anwar_Vahed.flac"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_06-Anwar_Vahed.wav"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_50-Kevin_Ashley[partial].flac"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_50-Kevin_Ashley[partial].wav"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-09_05-Fiona_Murphy.flac"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-09_05-Fiona_Murphy.wav"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_09-Natalia_Manola.flac"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_09-Natalia_Manola.wav"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_43-Juan_Bicarregui.flac"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_43-Juan_Bicarregui.wav"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-14_02-Simon_Hodson.flac"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-14_02-Simon_Hodson.wav"
        }
      ],
      "identifier": "./Policy and Implementation Review Interviews/Interview_Audio",
      "name": "Expert Interviews Audio Files"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-11_11-Anita_de_Waard.flac",
      "@type": "File",
      "contentSize": "57347219",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-11_11-Anita_de_Waard.flac",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Anita de Waard",
      "encodingFormat": "FLAC (Free Lossless Audio Codec)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/279",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-11_11-Anita_de_Waard.flac"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-11_11-Anita_de_Waard.wav",
      "@type": "File",
      "contentSize": "239478428",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-11_11-Anita_de_Waard.wav",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Anita de Waard",
      "encodingFormat": "Waveform Audio",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/6",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-11_11-Anita_de_Waard.wav"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_34-Michael_Ball.flac",
      "@type": "File",
      "contentSize": "63901469",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_34-Michael_Ball.flac",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Michael Ball",
      "encodingFormat": "FLAC (Free Lossless Audio Codec)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/279",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-13_34-Michael_Ball.flac"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_34-Michael_Ball.wav",
      "@type": "File",
      "contentSize": "248399508",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_34-Michael_Ball.wav",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Michael Ball",
      "encodingFormat": "Waveform Audio",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/6",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-13_34-Michael_Ball.wav"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_57-Carly_Strasser.flac",
      "@type": "File",
      "contentSize": "35848013",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_57-Carly_Strasser.flac",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Carly Strasser",
      "encodingFormat": "FLAC (Free Lossless Audio Codec)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/279",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-13_57-Carly_Strasser.flac"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_57-Carly_Strasser.wav",
      "@type": "File",
      "contentSize": "147636380",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-13_57-Carly_Strasser.wav",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Carly Strasser",
      "encodingFormat": "Waveform Audio",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/6",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-13_57-Carly_Strasser.wav"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-14_28-Patricia_Cruze.flac",
      "@type": "File",
      "contentSize": "69569303",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-14_28-Patricia_Cruze.flac",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Patricia Cruze",
      "encodingFormat": "FLAC (Free Lossless Audio Codec)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/279",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-14_28-Patricia_Cruze.flac"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-14_28-Patricia_Cruze.wav",
      "@type": "File",
      "contentSize": "344629896",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-14_28-Patricia_Cruze.wav",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Patricia Cruze",
      "encodingFormat": "Waveform Audio",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/6",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-14_28-Patricia_Cruze.wav"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-15_52-David_Carr.flac",
      "@type": "File",
      "contentSize": "40903581",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-15_52-David_Carr.flac",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with David Carr",
      "encodingFormat": "FLAC (Free Lossless Audio Codec)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/279",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-15_52-David_Carr.flac"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-15_52-David_Carr.wav",
      "@type": "File",
      "contentSize": "224346740",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-15_52-David_Carr.wav",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with David Carr",
      "encodingFormat": "Waveform Audio",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/6",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-15_52-David_Carr.wav"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_06-Anwar_Vahed.flac",
      "@type": "File",
      "contentSize": "63874559",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_06-Anwar_Vahed.flac",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Anwar Vahed",
      "encodingFormat": "FLAC (Free Lossless Audio Codec)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/279",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-16_06-Anwar_Vahed.flac"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_06-Anwar_Vahed.wav",
      "@type": "File",
      "contentSize": "327705242",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_06-Anwar_Vahed.wav",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Anwar Vahed",
      "encodingFormat": "Waveform Audio",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/6",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-16_06-Anwar_Vahed.wav"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_50-Kevin_Ashley[partial].flac",
      "@type": "File",
      "contentSize": "48753386",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_50-Kevin_Ashley[partial].flac",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Kevin Ashley",
      "encodingFormat": "FLAC (Free Lossless Audio Codec)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/279",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-16_50-Kevin_Ashley[partial].flac"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_50-Kevin_Ashley[partial].wav",
      "@type": "File",
      "contentSize": "278744572",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-24_09_2015-16_50-Kevin_Ashley[partial].wav",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Kevin Ashley",
      "encodingFormat": "Waveform Audio",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/6",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-24_09_2015-16_50-Kevin_Ashley[partial].wav"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-09_05-Fiona_Murphy.flac",
      "@type": "File",
      "contentSize": "86485429",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-09_05-Fiona_Murphy.flac",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Fiona Murphy",
      "encodingFormat": "FLAC (Free Lossless Audio Codec)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/279",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-25_09_2015-09_05-Fiona_Murphy.flac"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-09_05-Fiona_Murphy.wav",
      "@type": "File",
      "contentSize": "463684252",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-09_05-Fiona_Murphy.wav",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Fiona Murphy",
      "encodingFormat": "Waveform Audio",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/6",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-25_09_2015-09_05-Fiona_Murphy.wav"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_09-Natalia_Manola.flac",
      "@type": "File",
      "contentSize": "83348503",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_09-Natalia_Manola.flac",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Natalia Manola",
      "encodingFormat": "FLAC (Free Lossless Audio Codec)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/279",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-25_09_2015-13_09-Natalia_Manola.flac"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_09-Natalia_Manola.wav",
      "@type": "File",
      "contentSize": "424043172",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_09-Natalia_Manola.wav",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Natalia Manola",
      "encodingFormat": "Waveform Audio",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/6",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-25_09_2015-13_09-Natalia_Manola.wav"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_43-Juan_Bicarregui.flac",
      "@type": "File",
      "contentSize": "44904741",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_43-Juan_Bicarregui.flac",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Juan Bicarregui",
      "encodingFormat": "FLAC (Free Lossless Audio Codec)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/279",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-25_09_2015-13_43-Juan_Bicarregui.flac"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_43-Juan_Bicarregui.wav",
      "@type": "File",
      "contentSize": "243069834",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-13_43-Juan_Bicarregui.wav",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Juan Bicarregui",
      "encodingFormat": "Waveform Audio",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/6",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-25_09_2015-13_43-Juan_Bicarregui.wav"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-14_02-Simon_Hodson.flac",
      "@type": "File",
      "contentSize": "79799940",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-14_02-Simon_Hodson.flac",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Simon Hodson",
      "encodingFormat": "FLAC (Free Lossless Audio Codec)",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/279",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-25_09_2015-14_02-Simon_Hodson.flac"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-14_02-Simon_Hodson.wav",
      "@type": "File",
      "contentSize": "425747100",
      "path": "data/Policy and Implementation Review Interviews/Interview_Audio/Interview-25_09_2015-14_02-Simon_Hodson.wav",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Audio of interview with Simon Hodson",
      "encodingFormat": "Waveform Audio",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/6",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Interview-25_09_2015-14_02-Simon_Hodson.wav"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes",
      "description": "As part of the initial review for the project interviews were conducted with experts on data management planning and sharing policy and implementation. These are the written records and transcripts of those interviews. Most interviews conducted at the RDA Plenary in Paris 25-25 September 2015 ",
      "hasPart": [
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-11_11-Anita_de_Waard.rtf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-13_34-Michael_Ball.rtf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-13_57-Carly_Strasser.rtf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-14_28-Patricia_Cruze.rtf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-15_52-David_Carr.rtf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-16_06-Anwar_Vahed.rtf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-16_50-Kevin_Ashley[partial].rtf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-09_05-Fiona_Murphy.rtf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-13_09-Natalia_Manola.rtf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-13_43-Juan_Bicarregui.rtf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-14_02-Simon_Hodson.rtf"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_11_2015-16_00-Mathew-Harvey.rtf"
        }
      ],
      "identifier": "./Policy and Implementation Review Interviews/Interview_Notes",
      "name": "Data Management Expert Interview Notes"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-11_11-Anita_de_Waard.rtf",
      "@type": "File",
      "contentSize": "114629",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-11_11-Anita_de_Waard.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with Anita de Waard, RDA Paris",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/355",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-11_11-Anita_de_Waard.rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-13_34-Michael_Ball.rtf",
      "@type": "File",
      "contentSize": "384786",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-13_34-Michael_Ball.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with Michael Ball, RDA Paris",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-13_34-Michael_Ball.rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-13_57-Carly_Strasser.rtf",
      "@type": "File",
      "contentSize": "11092",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-13_57-Carly_Strasser.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with Carly Strasser, RDA Paris",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/50",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-13_57-Carly_Strasser.rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-14_28-Patricia_Cruze.rtf",
      "@type": "File",
      "contentSize": "406854",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-14_28-Patricia_Cruze.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with Patricia Cruze, RDA Paris",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-14_28-Patricia_Cruze.rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-15_52-David_Carr.rtf",
      "@type": "File",
      "contentSize": "340257",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-15_52-David_Carr.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with David Carr, RDA Paris",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-15_52-David_Carr.rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-16_06-Anwar_Vahed.rtf",
      "@type": "File",
      "contentSize": "99888",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-16_06-Anwar_Vahed.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with Anwar Vahed, RDA Paris",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/355",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-16_06-Anwar_Vahed.rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-16_50-Kevin_Ashley[partial].rtf",
      "@type": "File",
      "contentSize": "12771",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-16_50-Kevin_Ashley[partial].rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with Kevin Ashley, RDA Paris",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/50",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-24_09_2015-16_50-Kevin_Ashley[partial].rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-09_05-Fiona_Murphy.rtf",
      "@type": "File",
      "contentSize": "435251",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-09_05-Fiona_Murphy.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with Fiona Murphy, RDA Paris",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-09_05-Fiona_Murphy.rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-13_09-Natalia_Manola.rtf",
      "@type": "File",
      "contentSize": "451889",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-13_09-Natalia_Manola.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with Natalia Manola, RDA Paris",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-13_09-Natalia_Manola.rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-13_43-Juan_Bicarregui.rtf",
      "@type": "File",
      "contentSize": "100187",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-13_43-Juan_Bicarregui.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with Juan Bicarregui, RDA Paris",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/355",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-13_43-Juan_Bicarregui.rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-14_02-Simon_Hodson.rtf",
      "@type": "File",
      "contentSize": "468190",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-14_02-Simon_Hodson.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with Simon Hodson, RDA Paris",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-25_09_2015-14_02-Simon_Hodson.rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_11_2015-16_00-Mathew-Harvey.rtf",
      "@type": "File",
      "contentSize": "94235",
      "path": "data/Policy and Implementation Review Interviews/Interview_Notes/Interview-25_11_2015-16_00-Mathew-Harvey.rtf",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Record of interview with Mathew Harvey, by phone. No recording was made of this interview so these notes are the only record.",
      "encodingFormat": "Rich Text Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/53",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/Interview_Notes/Interview-25_11_2015-16_00-Mathew-Harvey.rtf"
    },
    {
      "@id": "data/Policy and Implementation Review Interviews/RDAInterviewQuestions.pdf",
      "@type": "File",
      "contentSize": "51648",
      "path": "data/Policy and Implementation Review Interviews/RDAInterviewQuestions.pdf",
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Interview prompt for interviews with RDM experts",
      "encodingFormat": "Acrobat PDF 1.3 - Portable Document Format",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/17",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Policy and Implementation Review Interviews/RDAInterviewQuestions.pdf"
    },
    {
      "@id": "data/Project Codes.txt",
      "@type": "File",
      "contentSize": "393",
      "path": "data/Project Codes.txt",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Three letter code that links each file to the relevant contributing project of the seven that made the inputs for this Pilot Project",
      "encodingFormat": "Plain Text File",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/x-fmt/111",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "Project Codes.txt"
    },
    {
      "@id": "RDA",
      "description": "International organisation for improving research data management practice",
      "identifier": "RDA",
      "name": "Research Data Alliance",
      "@type": [
        "Thing"
      ]
    },
    {
      "@id": "data/README.txt",
      "@type": "File",
      "contentSize": "3892",
      "path": "data/README.txt",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "README File for the data package. Contains some additional human-readable information and links. The CATALOG.html file is a better source of detailed information on each file and the relations between them.",
      "encodingFormat": "Plain Text File",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/x-fmt/111",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "README.txt"
    },
    {
      "@id": "data/SciDataCon Presentations",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "path": "data/SciDataCon Presentations",
      "description": "The Pilot Project submitted a session for the SciDataCon meeting in Denver in 2016 (http://www.scidatacon.org/2016/sessions/56/). A number of the Contributing Projects gave presentations alongside an outline of the initial findings from the Pilot. The separate slide decks and the submitted abstracts from each project are included.",
      "hasPart": [
        {
          "@id": "data/SciDataCon Presentations/AAA_20160913-IDRC-SciDataCon Presentation.pptx"
        },
        {
          "@id": "data/SciDataCon Presentations/HMP_HarassMap’s Data Management Project.pptx"
        },
        {
          "@id": "data/SciDataCon Presentations/IKC_Cath Traynor_Should Data be Shared (SciDataCon).pptx"
        },
        {
          "@id": "data/SciDataCon Presentations/TED_20160905-african-tobacco-data-woolfrey.pptx"
        },
        {
          "@id": "data/SciDataCon Presentations/AAA_Pilot_Project_Abstract.html"
        },
        {
          "@id": "data/SciDataCon Presentations/HMP_HarassMap_Abstract.html"
        },
        {
          "@id": "data/SciDataCon Presentations/IKC_Natural_Justice_Abstract.html"
        },
        {
          "@id": "data/SciDataCon Presentations/TED_Tobacco_Economics_Abstract.html"
        },
        {
          "@id": "data/SciDataCon Presentations/AAA_Session_Proposal.html"
        }
      ],
      "identifier": "./SciDataCon Presentations",
      "name": "Presentations given at SciDataCon Session",
      "relatedLink": "http://www.scidatacon.org/2016/sessions/56/"
    },
    {
      "@id": "data/SciDataCon Presentations/AAA_20160913-IDRC-SciDataCon Presentation.pptx",
      "@type": "File",
      "contentSize": "14594270",
      "path": "data/SciDataCon Presentations/AAA_20160913-IDRC-SciDataCon Presentation.pptx",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Presentation of the Pilot Project's Initial findings",
      "encodingFormat": "Microsoft Powerpoint for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/215",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "SciDataCon Presentations/AAA_20160913-IDRC-SciDataCon Presentation.pptx"
    },
    {
      "@id": "data/SciDataCon Presentations/AAA_Pilot_Project_Abstract.html",
      "@type": "File",
      "contentSize": "17085",
      "path": "data/SciDataCon Presentations/AAA_Pilot_Project_Abstract.html",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Abstract for the Pilot Project initial findings",
      "encodingFormat": "Hypertext Markup Language",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/96",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "SciDataCon Presentations/AAA_Pilot_Project_Abstract.html",
      "sameAs": "http://www.scidatacon.org/2016/sessions/56/paper/265/"
    },
    {
      "@id": "data/SciDataCon Presentations/AAA_Session_Proposal.html",
      "@type": "File",
      "contentSize": "8016",
      "path": "data/SciDataCon Presentations/AAA_Session_Proposal.html",
      "copyrightHolder": {
        "@id": "IDRC"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "description": "Session Proposal for SciDataCon",
      "encodingFormat": "Hypertext Markup Language",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/96",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "SciDataCon Presentations/AAA_Session_Proposal.html",
      "sameAs": "http://www.scidatacon.org/2016/sessions/56/"
    },
    {
      "@id": "data/SciDataCon Presentations/HMP_HarassMap_Abstract.html",
      "@type": "File",
      "contentSize": "5849",
      "path": "data/SciDataCon Presentations/HMP_HarassMap_Abstract.html",
      "copyrightHolder": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "creator": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "description": "Abstract for the HarassMap paper",
      "encodingFormat": "Hypertext Markup Language",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/96",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "SciDataCon Presentations/HMP_HarassMap_Abstract.html",
      "sameAs": "http://www.scidatacon.org/2016/sessions/56/paper/268/"
    },
    {
      "@id": "data/SciDataCon Presentations/HMP_HarassMap’s Data Management Project.pptx",
      "@type": "File",
      "contentSize": "4018305",
      "path": "data/SciDataCon Presentations/HMP_HarassMap’s Data Management Project.pptx",
      "copyrightHolder": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "creator": {
        "@id": "6e41be89-1635-4d96-b5e1-7d9d88049190"
      },
      "description": "Presentation of the DMP project and its experience",
      "encodingFormat": "Microsoft Powerpoint for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/215",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "SciDataCon Presentations/HMP_HarassMap’s Data Management Project.pptx"
    },
    {
      "@id": "data/SciDataCon Presentations/IKC_Cath Traynor_Should Data be Shared (SciDataCon).pptx",
      "@type": "File",
      "contentSize": "115730",
      "path": "data/SciDataCon Presentations/IKC_Cath Traynor_Should Data be Shared (SciDataCon).pptx",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "description": "Presentation of the IKC project and its experience",
      "encodingFormat": "Microsoft Powerpoint for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/215",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "SciDataCon Presentations/IKC_Cath Traynor_Should Data be Shared (SciDataCon).pptx"
    },
    {
      "@id": "data/SciDataCon Presentations/IKC_Natural_Justice_Abstract.html",
      "@type": "File",
      "contentSize": "7656",
      "path": "data/SciDataCon Presentations/IKC_Natural_Justice_Abstract.html",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-9661-487X"
      },
      "description": "Abstract for the Natural Justice paper",
      "encodingFormat": "Hypertext Markup Language",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/96",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "SciDataCon Presentations/IKC_Natural_Justice_Abstract.html",
      "sameAs": "http://www.scidatacon.org/2016/sessions/56/paper/271/"
    },
    {
      "@id": "data/SciDataCon Presentations/TED_20160905-african-tobacco-data-woolfrey.pptx",
      "@type": "File",
      "contentSize": "7513480",
      "path": "data/SciDataCon Presentations/TED_20160905-african-tobacco-data-woolfrey.pptx",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "description": "Presentation of the TED project and its experience",
      "encodingFormat": "Microsoft Powerpoint for Windows",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/215",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "SciDataCon Presentations/TED_20160905-african-tobacco-data-woolfrey.pptx"
    },
    {
      "@id": "data/SciDataCon Presentations/TED_Tobacco_Economics_Abstract.html",
      "@type": "File",
      "contentSize": "5880",
      "path": "data/SciDataCon Presentations/TED_Tobacco_Economics_Abstract.html",
      "copyrightHolder": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0001-8328-7091"
      },
      "description": "Abstract for the Tobacco Economics paper",
      "encodingFormat": "Hypertext Markup Language",
      "fileFormat": "http://www.nationalarchives.gov.uk/PRONOM/fmt/96",
      "license": {
        "@id": "https://creativecommons.org/licenses/by/4.0/"
      },
      "name": "SciDataCon Presentations/TED_Tobacco_Economics_Abstract.html",
      "sameAs": "http://www.scidatacon.org/2016/sessions/56/paper/275/"
    },
    {
      "@id": "a7b498c4-46fc-4e02-af5c-e72d4050eacb",
      "@type": "Person",
      "name": "Matthew Harvey"
    },
    {
      "@id": "a9baaf6c-c315-427e-a9a2-3a9bc06d0605",
      "@type": "Person",
      "name": "Le Dang Trung"
    },
    {
      "@id": "b9947255-54a2-4120-8845-faecf37ae2e8",
      "@type": "Person",
      "name": "Laura Foster"
    },
    {
      "@id": "cn@cameronneylon.net",
      "@type": "ContactPoint",
      "contactType": "customer service",
      "email": "cn@cameronneylon.net",
      "identifier": "cn@cameronneylon.net",
      "name": "Contact Cameron Neylon"
    },
    {
      "@id": "cnam",
      "@type": "Place",
      "URL": "http://www.cnam.fr/",
      "address": "292 Rue Saint-Martin, 75003 Paris, France",
      "description": "French Conservatory of Arts and Crafts and location of the 2015 RDA Plenary in Paris",
      "identifier": "cnam",
      "name": "Conservatoire National des arts et métiers"
    },
    {
      "@id": "d0924b9b-a9ec-4b7f-bc7a-6d2f0582b219",
      "@type": "Person",
      "name": "Danae Tapia"
    },
    {
      "@id": "d1d34769-134f-4747-99eb-4e8deeb140fa",
      "@type": "Person",
      "name": "Aïssa Diarra"
    },
    {
      "@id": "http://orcid.org/0000-0001-5250-7653",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0001-5250-7653",
      "name": "Juan Bicarregui"
    },
    {
      "@id": "http://orcid.org/0000-0001-7546-5978",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0001-7546-5978",
      "name": "Kevin Ashley"
    },
    {
      "@id": "http://orcid.org/0000-0001-8328-7091",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0001-8328-7091",
      "name": "Lynn Woolfrey"
    },
    {
      "@id": "http://orcid.org/0000-0001-8615-6652",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0001-8615-6652",
      "name": "Dora Canhos"
    },
    {
      "@id": "http://orcid.org/0000-0001-9592-2339",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0001-9592-2339",
      "name": "Carly Strasser"
    },
    {
      "@id": "http://orcid.org/0000-0002-0068-716X",
      "@type": "Person",
      "contactPoint": {
        "@id": "cn@cameronneylon.net"
      },
      "email": "cn@cameronneylon.net",
      "identifier": "http://orcid.org/0000-0002-0068-716X",
      "name": "Cameron Neylon"
    },
    {
      "@id": "http://orcid.org/0000-0002-3477-3082",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0002-3477-3082",
      "name": "Natalia Manola"
    },
    {
      "@id": "http://orcid.org/0000-0002-5595-3904",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0002-5595-3904",
      "name": "Anwar Vahed"
    },
    {
      "@id": "http://orcid.org/0000-0002-9034-4119",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0002-9034-4119",
      "name": "Anita de Waard"
    },
    {
      "@id": "http://orcid.org/0000-0002-9661-487X",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0002-9661-487X",
      "name": "Cath Traynor"
    },
    {
      "@id": "http://orcid.org/0000-0003-0211-4549",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0003-0211-4549",
      "name": "Pascal Aventurier"
    },
    {
      "@id": "http://orcid.org/0000-0003-1435-307X",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0003-1435-307X",
      "name": "David Carr"
    },
    {
      "@id": "http://orcid.org/0000-0003-1693-1240",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0003-1693-1240",
      "name": "Fiona Murphy"
    },
    {
      "@id": "http://orcid.org/0000-0003-3179-7270",
      "@type": "Person",
      "identifier": "http://orcid.org/0000-0003-3179-7270",
      "name": "Simon Hodson"
    },
    {
      "@id": "bibo:interviewee",
      "sameAs": "http://neologism.ecs.soton.ac.uk/bibo.html#interviewee",
      "@type": [
        "Thing"
      ]
    },
    {
      "@id": "bibo:interviewer",
      "sameAs": "http://neologism.ecs.soton.ac.uk/bibo.html#interviewer",
      "@type": [
        "Thing"
      ]
    },
    {
      "@id": "https://creativecommons.org/licenses/by/4.0/",
      "description": "Attribution 4.0 International (CC BY 4.0)\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\nYou are free to:\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\nShare — copy and redistribute the material in any medium or format\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\nAdapt — remix, transform, and build upon the material\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\nfor any purpose, even commercially.\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n This license is acceptable for Free Cultural Works.\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\nThe licensor cannot revoke these freedoms as long as you follow the license terms.\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\nUnder the following terms:\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\nAttribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.\r\r\r\r\n\r\r\r\r\n\r\r\r\r\n\r\r\r\r\nNo additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.",
      "identifier": "https://creativecommons.org/licenses/by/4.0/",
      "name": "CC BY 4.0",
      "@type": [
        "Thing"
      ]
    },
    {
      "@id": "https://doi.org/10.3897/rio.2.e8880",
      "@type": [
        "Project",
        "Organization"
      ],
      "funder": {
        "@id": "IDRC"
      },
      "identifier": [
        "https://doi.org/10.3897/rio.2.e8880",
        "doi.org/10.3897/rio.2.e8880"
      ],
      "name": "Exploring the opportunities and challenges of implementing open research strategies within development institutions"
    },
    {
      "@id": "https://dx.doi.org/10.5281/zenodo.844394",
      "@type": "Dataset",
      "contactPoint": {
        "@id": "cn@cameronneylon.net"
      },
      "path": "./",
      "contributor": {
        "@id": "https://doi.org/10.3897/rio.2.e8880"
      },
      "creator": {
        "@id": "http://orcid.org/0000-0002-0068-716X"
      },
      "datePublished": "2017",
      "description": "Data relating to the IDRC funded project (described in https://doi.org/10.3897/rio.2.e8880) to examine data management policies and implementation for development funders. The project involved two parts: a review based on desk work and expert interviews and seven case studies of existing IDRC-funded projects. The case studies were supported by an Introductory Workshop in which the idea of data was examined and the issues involved in sharing discussed in detail. This was followed by an implementation phase in which the projects were supported in developing Data Management Plans. The performance against those plans was then assessed both by the participants and as part of the overall project to generate case studies that are to be published as part of the related RIO Journal Collection. The final project report will also be part of the same collection.",
      "hasPart": [
        {
          "@id": "data/Project Codes.txt"
        },
        {
          "@id": "data/README.txt"
        },
        {
          "@id": "data/Data Management Planning"
        },
        {
          "@id": "data/Final_Project_Workshop_Materials"
        },
        {
          "@id": "data/Final_Project_Workshop_Presentations"
        },
        {
          "@id": "data/Introductory_Data_Workshop_Materials"
        },
        {
          "@id": "data/Introductory_Workshop_Presentations"
        },
        {
          "@id": "data/Policy and Implementation Review Interviews"
        },
        {
          "@id": "data/SciDataCon Presentations"
        }
      ],
      "identifier": [
        "https://dx.doi.org/10.5281/zenodo.844394",
        "dx.doi.org/10.5281/zenodo.844394"
      ],
      "name": "Dataset for IDRC Project: Exploring the opportunities and challenges of implementing open research strategies within development institutions",
      "publisher": {
        "@id": "IDRC"
      },
      "relatedLink": [
        "https://doi.org/10.3897/rio.3.e14673",
        "https://riojournal.com/collection/18/"
      ],
      "distribution": [
        {
          "@id": "https://data.research.uts.edu.au/examples/ro-crate/0.2Data_Package-IDRC_Opportunities_and_Challenges_Open_Research_Strategies/Data_Package-IDRC_Opportunities_and_Challenges_Open_Research_Strategies.zip"
        }
      ]
    },
    {
      "@id": "https://www.linkedin.com/in/michael-ball-19236819",
      "@type": "Person",
      "identifier": "https://www.linkedin.com/in/michael-ball-19236819",
      "name": "Michael Ball"
    },
    {
      "@id": "https://www.linkedin.com/in/patricia-trisha-cruse-77a2b39/",
      "@type": "Person",
      "identifier": "https://www.linkedin.com/in/patricia-trisha-cruse-77a2b39/",
      "name": "Patricia Cruze"
    },
    {
      "@id": "https://data.research.uts.edu.au/examples/ro-crate/0.2Data_Package-IDRC_Opportunities_and_Challenges_Open_Research_Strategies/Data_Package-IDRC_Opportunities_and_Challenges_Open_Research_Strategies.zip",
      "contentUrl": "https://data.research.uts.edu.au/examples/ro-crate/0.2Data_Package-IDRC_Opportunities_and_Challenges_Open_Research_Strategies/Data_Package-IDRC_Opportunities_and_Challenges_Open_Research_Strategies.zip",
      "@type": "DataDownload",
      "encodingFormat": "zip"
    }
  ]
}


def openAire_datasets(doi:str):
        openAireURL = "https://api.openaire.eu/search/datasets"

        payload = {
                'doi': doi,
                'format': "json",
                'size':100
        }
        response = requests.get(openAireURL, params=payload).json()
        #f = open("Massive-ROs-Creator\Enrichment.json", "w")
        #f.write(json.dumps(response, indent=4, sort_keys=True))
        #f.close()
        #print (response)
        if '"results": null' in str(response):
                return None
        else:
                #print(type(response))
                return response
        
        

def openAire_pub(doi:str):
        openAireURL = "https://api.openaire.eu/search/publications"

        payload = {
                'doi': doi,
                'format': "json",
                'size':100
        }
        response = requests.get(openAireURL, params=payload).json()
        
        #print (response)
        if "'results': None" in str(response):
                return None
        else:
                #print(type(response))
                return response

def enrich_RO (RO: dict):
  doi = ""
  for dictionary in RO.get("@graph"):
    try:
      found = "Dataset" in dictionary.get("@type") and "https" in dictionary.get("@id")
      if found:
        url = dictionary.get("@id")
        #print (url)
        if "archive.sigma" in url:
          doi = url[url.find("id%3D")+5:].replace("%2F","/")
        else:
          doi = url[url.find("//")+2:]
          doi = doi[doi.find("/")+1:]
        #print(doi)
        break
    except:
      continue
  #print(doi)
  enrichment_RO_raw = openAire_datasets(doi)
  ro = {}
  if enrichment_RO_raw != None and not "'results': None" in str(enrichment_RO_raw):
    #print(enrichment_RO_raw)
    
    enrichment_RO_raw = enrichment_RO_raw.get("response").get("results").get("result")[0]
    #print (enrichment_RO_raw)

    ro["date_of_collection"] = enrichment_RO_raw.get("header").get("dri:dateOfCollection").get("$")
    ro["date_of_transformation"] = enrichment_RO_raw.get("header").get("dri:dateOfTransformation").get("$")
    enrichment_RO_raw = enrichment_RO_raw.get("metadata").get("oaf:entity").get("oaf:result")

    if "classname" in enrichment_RO_raw.get("bestaccessright").keys() : 
            ro["bestaccessright"] = enrichment_RO_raw.get("bestaccessright").get("classname")

    if "children" in enrichment_RO_raw.keys():
            if "result" in enrichment_RO_raw.get("children").keys():
                    results = []
                    for result in enrichment_RO_raw.get("children").get("result"):
                            dateofacceptance = ""
                            publisher = ""
                            if "dateofacceptance" in result.keys():
                                    dateofacceptance = result.get("dateofacceptance").get("$")
                            if "publisher" in result.keys():
                                    publisher = result.get("publisher").get("$")
                            result_aux = {"date_of_acceptance":dateofacceptance, "publisher":publisher}
                            results.append(result_aux)
                            results.append(result_aux)
                    ro["Children Results"] = results
    #print (enrichment_RO_raw.get("collectedfrom"))
    collectedfrom = []

    if type(enrichment_RO_raw.get("collectedfrom"))==list and "collectedfrom" in enrichment_RO_raw.keys():
            collectedfrom = []
            for source in enrichment_RO_raw.get("collectedfrom"):
                    name = ""
                    #print (source)
                    if type(source)==dict and "@name" in source.keys():
                            #print (source)
                            name = source.get("@name")
                            #print (name)
                            collectedfrom.append(name)
                  
            ro["Collected From"] = collectedfrom
    elif (enrichment_RO_raw.get("collectedfrom"))==dir:
            name = enrichment_RO_raw.get("collectedfrom").get("@name")
            collectedfrom.append(name)


    if "creator" in enrichment_RO_raw.keys():
            if not ro.get("Creator") == None:
                    creator_list = ro.get("Creator")
                    #print (creator_list)
            else:
                    creator_list = []
            #print(enrichment_RO_raw.get("creator"))
            if type(enrichment_RO_raw.get("creator")) == list:
              for creator in enrichment_RO_raw.get("creator"):
              
                      #print (creator)
                      if type(creator) == dict:
                              creator_list.append(creator)
              #print (creator_list)
            elif type(enrichment_RO_raw.get("creator"))==dict:
              creator_list.append(enrichment_RO_raw.get("creator"))
            ro["Creator"] = creator_list
    ####################All creator ????????????


    if "language" in  enrichment_RO_raw.keys():
            language = ""
            if "@classname" in enrichment_RO_raw.get("language").keys():
                    language = enrichment_RO_raw.get("language").get("@classname")
            ro["language"] = language

    if "publisher" in enrichment_RO_raw.keys():
            publisher = enrichment_RO_raw.get("publisher").get("$")
            ro["publisher"] = publisher

    if "resourcetype" in enrichment_RO_raw.keys():
            resourcetype = enrichment_RO_raw.get("resourcetype").get("@classname")
            ro["resourcetype"] = publisher

    if "subject" in enrichment_RO_raw.keys():
            subject_list = []
            for subject in enrichment_RO_raw.get("subject"):
                    name = subject.get("$")
                    #print (name)
                    if name not in subject_list:
                            subject_list.append(name)
            ro["research area"] = subject_list
  
############################################## Creation of the new RO-Crate ###################################################

  for dictionary in RO.get("@graph"):

    try:
      found = "Dataset" in dictionary.get("@type") and "https" in dictionary.get("@id")
      if found:
        RO["@graph"].remove(dictionary)
        #print(dictionary)
        for creator in ro["Creator"]:
          
          if type(dictionary.get("creator")) == list:
            aux_bool = False

            for creator_dict in dictionary.get("creator"):

               if creator.get("@orcid_pending").upper() in creator_dict.get("@id").upper():
                 aux_bool = True
                 print("We are here")

              
            if not (aux_bool):
              dictionary["creator"].append({"@id":"http://orcid.org/"+creator.get("@orcid_pending")})
          elif type(dictionary.get("creator")) == dict and creator.get("@orcid_pending").upper() not in dictionary.get("creator").get("@id").upper():
            dictionary["creator"] = [dictionary.get("creator"),{"@id":"http://orcid.org/"+creator.get("@orcid_pending")}]
      #print (dictionary)
      #print (RO["@graph"])
      if type(dictionary.get('publisher')) == dict and not ro.get('publisher') in dictionary.get('publisher').get('@id'):
        dictionary['publisher'] = [dictionary.get('publisher'),{'@id': ro.get('publisher')}]
      elif type(dictionary.get('publisher')) == list:
        aux_bool = False
        for publisher in dictionary.get('publisher'):
          if ro.get('publisher') in publisher.get('@id'):
            aux_bool = True
        if not (aux_bool):
          dictionary['publisher'].append({'@id': ro.get('publisher')})
        date = ro.get("Children Results")[0].get('date_of_acceptance')
        dictionary['datePublished'] = date

        dictionary['dateCreated'] = ro.get('date_of_collection')
        dictionary['dateModified'] = ro.get('date_of_transformation')
        RO["@graph"].append(dictionary)
      #print (RO["@graph"])
    except:
      pass

  print(ro)
  return (RO)
  #print (ro)