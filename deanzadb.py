class Course:
    def __init__(self, name, category, difficulty, credits, required = None, combinations=None, weight = None):
        self.name = name
        self.category = category
        self.difficulty = difficulty
        self.credits = credits
        self.required = 0 if required is None else required
        self.combinations = [] if combinations is None else combinations
       

course_area_1a = Course("EWRT 1A / 1AH", "English Composition", 1, 5,1)
english_comm = [course_area_1a]


course_comm_9 = Course("COMM 9 / 9H", "Critical Thinking-English Composition", 1, 5)
course_ewrt_2 = Course("EWRT 2 / 2H", "Critical Thinking-English Composition", 1, 5)
course_phil_3 = Course("PHIL 3", "Critical Thinking-English Composition", 1, 5)

english_composition = [course_comm_9, course_ewrt_2, course_phil_3]

math_1 = Course("MATH 1A / 1AH", "Mathematics", 2, 5)
math_2 = Course("MATH 1B / 1BH", "Mathematics", 2, 5)
math_3 = Course("MATH 1C / 1CH", "Mathematics", 2, 5)
math_4 = Course("MATH 1D / 1DH", "Mathematics", 2, 5)
math_5 = Course("MATH 2A / 2AH", "Mathematics", 2, 5)
math_6 = Course("MATH 2B / 2BH", "Mathematics", 2, 5)
math_7 = Course("MATH 10 / 10H", "Mathematics", 1, 5)
math_8 = Course("MATH 12 ", "Mathematics", 2, 5)
math_9 = Course("MATH 22 / 22H", "Mathematics", 1, 5)

mathematics = [math_1, math_2, math_3, math_4, math_5, math_6, math_7, math_8, math_9]

arts_1a = Course("ARTS 1A", "Arts", 1, 4)
arts_1b = Course("ARTS 1B", "Arts", 1, 4)
arts_2a = Course("ARTS 2A", "Arts", 1, 4)
arts_2b = Course("ARTS 2B", "Arts", 1, 4)
arts_2c = Course("ARTS 2C", "Arts", 1, 4)
arts_2d = Course("ARTS 2D", "Arts", 1, 4)
arts_2f = Course("ARTS 2F", "Arts", 1, 4)
arts_2g = Course("ARTS 2G", "Arts", 1, 4)
arts_2h = Course("ARTS 2H", "Arts", 1, 4)
arts_2j = Course("ARTS 2J", "Arts", 1, 4)
arts_3tc = Course("ARTS 3TC#", "Arts", 1, 4)
arts_3te = Course("ARTS 3TE", "Arts", 1, 4)
asam_40 = Course("ASAM 40", "Arts", 1, 4)
ceth_13 = Course("CETH 13", "Arts", 1, 4)
chlx_13 = Course("CHLX 13", "Arts", 1, 4)
danc_38a = Course("DANC 38A", "Arts", 1, 4)
es_3 = Course("E S 3#", "Arts", 1, 4)
ftv_1 = Course("F/TV 1 / 1H", "Arts", 1, 4)
ftv_2a = Course("F/TV 2A#* / 2AH#*", "Arts", 1, 4)
ftv_2aw = Course("F/TV 2AW#* / 2AWH#*", "Arts", 1, 4)
ftv_2b = Course("F/TV 2B#* / 2BH#*", "Arts", 1, 4)
ftv_2bw = Course("F/TV 2BW#* / 2BWH#*", "Arts", 1, 4)
ftv_2c = Course("F/TV 2C#* / 2CH#*", "Arts", 1, 4)
ftv_2cw = Course("F/TV 2CW#* / 2CWH#*", "Arts", 1, 4)
humi_1 = Course("HUMI 1# / 1H#", "Arts", 1, 4)
humi_15 = Course("HUMI 15", "Arts", 1, 4)
intl_21 = Course("INTL 21", "Arts", 1, 4)
intl_22 = Course("INTL 22", "Arts", 1, 4)
musi_1a = Course("MUSI 1A", "Arts", 1, 4)
musi_1b = Course("MUSI 1B", "Arts", 1, 4)
musi_1c = Course("MUSI 1C", "Arts", 1, 4)
musi_1d = Course("MUSI 1D", "Arts", 1, 4)
nais_13 = Course("NAIS 13", "Arts", 1, 4)
phtg_7 = Course("PHTG 7", "Arts", 1, 4)
phtg_21 = Course("PHTG 21", "Arts", 1, 4)
thea_1 = Course("THEA 1", "Arts", 1, 4)
wmst_3c = Course("WMST 3C#", "Arts", 1, 4)

# Add the Arts courses to the 'art' list
art = [arts_1a, arts_1b, arts_2a, arts_2b, arts_2c, arts_2d, arts_2f, arts_2g, arts_2h, arts_2j, arts_3tc, arts_3te,
       asam_40, ceth_13, chlx_13, danc_38a, es_3, ftv_1 , ftv_2a , ftv_2aw , ftv_2b,
       ftv_2bw , ftv_2c , ftv_2cw , humi_1 , humi_15, intl_21, intl_22, musi_1a,
       musi_1b, musi_1c, musi_1d, nais_13, phtg_7, phtg_21, thea_1, wmst_3c]

afam_11 = Course("AFAM 11#", "Humanities", 1, 4)
afam_25 = Course("AFAM 25#", "Humanities", 1, 4)
asam_20 = Course("ASAM 20", "Humanities", 1, 4)
asam_21 = Course("ASAM 21", "Humanities", 1, 4)
asam_22 = Course("ASAM 22#", "Humanities", 1, 4)
asam_32 = Course("ASAM 32", "Humanities", 1, 4)
asam_41 = Course("ASAM 41", "Humanities", 1, 4)
ceth_8 = Course("CETH 8#", "Humanities", 1, 4)
ceth_19 = Course("CETH 19#", "Humanities", 1, 4)
chlx_26 = Course("CHLX 26#", "Humanities", 1, 4)
esl_6 = Course("ESL 6", "Humanities", 1, 4)
elit_8 = Course("ELIT 8", "Humanities", 1, 4)
elit_10 = Course("ELIT 10 / 10H", "Humanities", 1, 4)
elit_11 = Course("ELIT 11", "Humanities", 1, 4)
elit_12 = Course("ELIT 12", "Humanities", 1, 4)
elit_17 = Course("ELIT 17 / 17H", "Humanities", 1, 4)
elit_19 = Course("ELIT 19", "Humanities", 1, 4)
elit_21 = Course("ELIT 21", "Humanities", 1, 4)
elit_22 = Course("ELIT 22", "Humanities", 1, 4)
elit_24 = Course("ELIT 24", "Humanities", 1, 4)
elit_28 = Course("ELIT 28", "Humanities", 1, 4)
elit_38 = Course("ELIT 38", "Humanities", 1, 4)
elit_39 = Course("ELIT 39", "Humanities", 1, 4)
elit_40 = Course("ELIT 40", "Humanities", 1, 4)
elit_41 = Course("ELIT 41 / 41H", "Humanities", 1, 4)
elit_46a = Course("ELIT 46A / 46AH", "Humanities", 1, 4)
elit_46b = Course("ELIT 46B / 46BH", "Humanities", 1, 4)
elit_46c = Course("ELIT 46C / 46CH", "Humanities", 1, 4)
elit_47a = Course("ELIT 47A", "Humanities", 1, 4)
elit_47b = Course("ELIT 47B", "Humanities", 1, 4)
elit_48a = Course("ELIT 48A / 48AH", "Humanities", 1, 4)
elit_48b = Course("ELIT 48B / 48BH", "Humanities", 1, 4)
elit_48c = Course("ELIT 48C / 48CH", "Humanities", 1, 4)
ewrt_1c = Course("EWRT 1C", "Humanities", 1, 4)
ftv_2a = Course("FTV 2A#* / 2AH#*", "Humanities", 1, 4)
ftv_2aw = Course("FTV 2AW#* / 2AWH#", "Humanities", 1, 4)
ftv_2b = Course("FTV 2B#* / 2BH#*", "Humanities", 1, 4)
ftv_2bw = Course("FTV 2BW#* / 2BWH#*", "Humanities", 1, 4)
ftv_2c = Course("FTV 2C#* / 2CH#", "Humanities", 1, 4)
ftv_2cw = Course("FTV 2CW#* / 2CWH#", "Humanities", 1, 4)
fren_3 = Course("FREN 3", "Humanities", 1, 4)
germ_3 = Course("GERM 3", "Humanities", 1, 4)
germ_4 = Course("GERM 4", "Humanities", 1, 4)
hndi_3 = Course("HNDI 3", "Humanities", 1, 4)
hist_3a = Course("HIST 3A# / 3AH#", "Humanities", 1, 4)
hist_3b = Course("HIST 3B# / 3BH#", "Humanities", 1, 4)
hist_3c = Course("HIST 3C# / 3CH#", "Humanities", 1, 4)
hist_6a = Course("HIST 6A# / 6AH#", "Humanities", 1, 4)
hist_6b = Course("HIST 6B# / 6BH#", "Humanities", 1, 4)
hist_6c = Course("HIST 6C# / 6CH#", "Humanities", 1, 4)
hist_17a = Course("HIST 17A# / 17AH#", "Humanities", 1, 4)
hist_17b = Course("HIST 17B# / 17BH#", "Humanities", 1, 4)
hist_17c = Course("HIST 17C# / 17CH#", "Humanities", 1, 4)
humi_1 = Course("HUMI 1# / 1H#", "Humanities", 1, 4)
humi_2 = Course("HUMI 2", "Humanities", 1, 4)
humi_5 = Course("HUMI 5", "Humanities", 1, 4)
humi_6 = Course("HUMI 6", "Humanities", 1, 4)
humi_7 = Course("HUMI 7", "Humanities", 1, 4)
humi_9 = Course("HUMI 9 / 9H", "Humanities", 1, 4)
humi_10 = Course("HUMI 10", "Humanities", 1, 4)
humi_13 = Course("HUMI 13", "Humanities", 1, 4)
humi_16 = Course("HUMI 16", "Humanities", 1, 4)
humi_18 = Course("HUMI 18 / 18H", "Humanities", 1, 4)
humi_20 = Course("HUMI 20", "Humanities", 1, 4)
ics_35 = Course("ICS 35", "Humanities", 1, 4)
intl_16 = Course("INTL 16", "Humanities", 1, 4)
ital_3 = Course("ITAL 3", "Humanities", 1, 4)
japn_3 = Course("JAPN 3", "Humanities", 1, 4)
japn_4 = Course("JAPN 4", "Humanities", 1, 4)
japn_5 = Course("JAPN 5", "Humanities", 1, 4)
japn_6 = Course("JAPN 6", "Humanities", 1, 4)
kore_3 = Course("KORE 3 / 3H", "Humanities", 1, 4)
ling_1 = Course("LING 1", "Humanities", 1, 4)
mand_3 = Course("MAND 3", "Humanities", 1, 4)
mand_4 = Course("MAND 4", "Humanities", 1, 4)
mand_5 = Course("MAND 5", "Humanities", 1, 4)
mand_6 = Course("MAND 6", "Humanities", 1, 4)
nais_14 = Course("NAIS 14", "Humanities", 1, 4)
nais_15 = Course("NAIS 15", "Humanities", 1, 4)
pers_3 = Course("PERS 3", "Humanities", 1, 4)
phil_1 = Course("PHIL 1", "Humanities", 1, 4)
phil_2 = Course("PHIL 2", "Humanities", 1, 4)
phil_8 = Course("PHIL 8 / 8H", "Humanities", 1, 4)
phil_11 = Course("PHIL 11", "Humanities", 1, 4)
phil_20a = Course("PHIL 20A", "Humanities", 1, 4)
phil_20b = Course("PHIL 20B", "Humanities", 1, 4)
phil_20c = Course("PHIL 20C", "Humanities", 1, 4)
phil_24 = Course("PHIL 24", "Humanities", 1, 4)
phil_30 = Course("PHIL 30", "Humanities", 1, 4)
phil_49 = Course("PHIL 49", "Humanities", 1, 4)
russ_3 = Course("RUSS 3", "Humanities", 1, 4)
sign_3 = Course("SIGN 3", "Humanities", 1, 4)
span_3 = Course("SPAN 3", "Humanities", 1, 4)
span_4 = Course("SPAN 4", "Humanities", 1, 4)
span_5 = Course("SPAN 5", "Humanities", 1, 4)
span_6 = Course("SPAN 6", "Humanities", 1, 4)
viet_3 = Course("VIET 3", "Humanities", 1, 4)
viet_4 = Course("VIET 4", "Humanities", 1, 4)
viet_5 = Course("VIET 5", "Humanities", 1, 4)
viet_6 = Course("VIET 6", "Humanities", 1, 4)
wmst_8 = Course("WMST 8#", "Humanities", 1, 4)
wmst_21 = Course("WMST 21", "Humanities", 1, 4)
wmst_22 = Course("WMST 22#", "Humanities", 1, 4)
wmst_25 = Course("WMST 25#", "Humanities", 1, 4)
wmst_26 = Course("WMST 26#", "Humanities", 1, 4)
wmst_27 = Course("WMST 27#", "Humanities", 1, 4)
wmst_29 = Course("WMST 29#", "Humanities", 1, 4)
wmst_31 = Course("WMST 31#", "Humanities", 1, 4)
wmst_49 = Course("WMST 49", "Humanities", 1, 4)

# Add the humanities courses to the appropriate list
humanities = [
    afam_11, afam_25, asam_20, asam_21, asam_22, asam_32, asam_41,
    ceth_8, ceth_19, chlx_26, esl_6, elit_8, elit_10 , elit_11,
    elit_12, elit_17 , elit_19, elit_21, elit_22, elit_24, elit_28,
    elit_38, elit_39, elit_40, elit_41 , elit_46a ,
    elit_46b , elit_46c , elit_47a, elit_47b, elit_48a,
     elit_48b, elit_48c, ewrt_1c, ftv_2a,
     ftv_2aw, ftv_2b , ftv_2bw, ftv_2c,
     ftv_2cw , fren_3, germ_3, germ_4, hndi_3, hist_3a,
     hist_3b, hist_3c, hist_6a,
    hist_6b , hist_6c, hist_17a, hist_17b,
     hist_17c, humi_1 , humi_2, humi_5, humi_6,
    humi_7, humi_9, humi_10, humi_13, humi_16, humi_18,
    humi_20, ics_35, intl_16, ital_3, japn_3, japn_4, japn_5, japn_6, kore_3, 
    ling_1, mand_3, mand_4, mand_5, mand_6, nais_14, nais_15, pers_3,
    phil_1, phil_2, phil_8, phil_11, phil_20a, phil_20b, phil_20c,
    phil_24, phil_30, phil_49, russ_3, sign_3, span_3, span_4, span_5, span_6,
    viet_3, viet_4, viet_5, viet_6, wmst_8, wmst_21, wmst_22, wmst_25, wmst_26,
    wmst_27, wmst_29, wmst_31, wmst_49
]

admj_29 = Course("ADMJ 29", "Social Science", 1, 4)
afam_10 = Course("AFAM 10", "Social Science", 1, 4)
afam_11 = Course("AFAM 11#", "Social Science", 1, 4)
afam_12a = Course("AFAM 12A", "Social Science", 1, 4)
afam_12b = Course("AFAM 12B", "Social Science", 1, 4)
afam_25 = Course("AFAM 25#", "Social Science", 1, 4)
anth_2 = Course("ANTH 2 / 2H", "Social Science", 1, 4)
anth_3 = Course("ANTH 3", "Social Science", 1, 4)
anth_4 = Course("ANTH 4", "Social Science", 1, 4)
anth_5 = Course("ANTH 5", "Social Science", 1, 4)
anth_6 = Course("ANTH 6", "Social Science", 1, 4)
anth_8 = Course("ANTH 8", "Social Science", 1, 4)
anth_12 = Course("ANTH 12", "Social Science", 1, 4)
arts_3tc = Course("ARTS 3TC#", "Social Science", 1, 4)
asam_1 = Course("ASAM 1", "Social Science", 1, 4)
asam_10 = Course("ASAM 10", "Social Science", 1, 4)
asam_11 = Course("ASAM 11", "Social Science", 1, 4)
asam_12 = Course("ASAM 12", "Social Science", 1, 4)
asam_13 = Course("ASAM 13", "Social Science", 1, 4)
asam_22 = Course("ASAM 22#", "Social Science", 1, 4)
asam_30 = Course("ASAM 30", "Social Science", 1, 4)
asam_42a = Course("ASAM 42A", "Social Science", 1, 4)
asam_42b = Course("ASAM 42B", "Social Science", 1, 4)
cd_10g = Course("C D 10G", "Social Science", 1, 4)
cd_10h = Course("C D 10H", "Social Science", 1, 4)
cd_12 = Course("C D 12", "Social Science", 1, 4)
ceth_8 = Course("CETH 8#", "Social Science", 1, 4)
ceth_10 = Course("CETH 10", "Social Science", 1, 4)
ceth_11 = Course("CETH 11", "Social Science", 1, 4)
ceth_19 = Course("CETH 19#", "Social Science", 1, 4)
ceth_29 = Course("CETH 29", "Social Science", 1, 4)
chlx_10 = Course("CHLX 10", "Social Science", 1, 4)
chlx_11 = Course("CHLX 11", "Social Science", 1, 4)
chlx_12 = Course("CHLX 12", "Social Science", 1, 4)
chlx_26 = Course("CHLX 26#", "Social Science", 1, 4)
comm_7 = Course("COMM 7 / 7H", "Social Science", 1, 4)
econ_1 = Course("ECON 1 / 1H", "Social Science", 1, 4)
econ_2 = Course("ECON 2 / 2H", "Social Science", 1, 4)
econ_3 = Course("ECON 3 / 3H", "Social Science", 1, 4)
econ_4 = Course("ECON 4", "Social Science", 1, 4)
econ_5 = Course("ECON 5", "Social Science", 1, 4)
es_1 = Course("E S 1", "Social Science", 1, 4)
es_3 = Course("E S 3#", "Social Science", 1, 4)
es_4 = Course("E S 4", "Social Science", 1, 4)
ftv_10 = Course("F/TV 10", "Social Science", 1, 4)
ftv_10h = Course("F/TV 10H", "Social Science", 1, 4)
geo_4 = Course("GEO 4", "Social Science", 1, 4)
geo_5 = Course("GEO 5", "Social Science", 1, 4)
geo_10 = Course("GEO 10", "Social Science", 1, 4)
hist_3a = Course("HIST 3A# / 3AH#", "Social Science", 1, 4)
hist_3b = Course("HIST 3B# / 3BH#", "Social Science", 1, 4)
hist_3c = Course("HIST 3C#", "Social Science", 1, 4)
hist_3ch = Course("HIST 3CH#", "Social Science", 1, 4)
hist_6a = Course("HIST 6A# / 6AH#", "Social Science", 1, 4)
hist_6b = Course("HIST 6B# / 6BH#", "Social Science", 1, 4)
hist_6c = Course("HIST 6C#", "Social Science", 1, 4)
hist_6ch = Course("HIST 6CH#", "Social Science", 1, 4)
hist_7a = Course("HIST 7A", "Social Science", 1, 4)
hist_7b = Course("HIST 7B", "Social Science", 1, 4)
hist_9 = Course("HIST 9 / 9H", "Social Science", 1, 4)
hist_10 = Course("HIST 10 / 10H", "Social Science", 1, 4)
hist_16a = Course("HIST 16A", "Social Science", 1, 4)
hist_16b = Course("HIST 16B", "Social Science", 1, 4)
hist_17a = Course("HIST 17A# / 17AH#", "Social Science", 1, 4)
hist_17b = Course("HIST 17B# / 17BH#", "Social Science", 1, 4)
hist_17c = Course("HIST 17C# / 17CH#", "Social Science", 1, 4)
hist_18a = Course("HIST 18A", "Social Science", 1, 4)
hist_18b = Course("HIST 18B", "Social Science", 1, 4)
hist_19a = Course("HIST 19A", "Social Science", 1, 4)
hist_19b = Course("HIST 19B", "Social Science", 1, 4)
huma_10 = Course("HUMA 10 / 10H", "Social Science", 1, 4)
ics_7 = Course("ICS 7", "Social Science", 1, 4)
ics_7h = Course("ICS 7H", "Social Science", 1, 4)
ics_16a = Course("ICS 16A", "Social Science", 1, 4)
ics_16b = Course("ICS 16B", "Social Science", 1, 4)
ics_17 = Course("ICS 17 / 17H", "Social Science", 1, 4)
ics_19 = Course("ICS 19", "Social Science", 1, 4)
ics_25 = Course("ICS 25", "Social Science", 1, 4)
ics_26 = Course("ICS 26", "Social Science", 1, 4)
ics_27 = Course("ICS 27 / 27H", "Social Science", 1, 4)
ics_36 = Course("ICS 36", "Social Science", 1, 4)
ics_37 = Course("ICS 37", "Social Science", 1, 4)
ics_38a = Course("ICS 38A", "Social Science", 1, 4)
ics_38b = Course("ICS 38B", "Social Science", 1, 4)
ics_47 = Course("ICS 47", "Social Science", 1, 4)
intl_5 = Course("INTL 5", "Social Science", 1, 4)
intl_8 = Course("INTL 8", "Social Science", 1, 4)
intl_33 = Course("INTL 33", "Social Science", 1, 4)
jour_2 = Course("JOUR 2", "Social Science", 1, 4)
knes_47 = Course("KNES 47", "Social Science", 1, 4)
nais_11 = Course("NAIS 11", "Social Science", 1, 4)
nais_12 = Course("NAIS 12", "Social Science", 1, 4)
nais_16 = Course("NAIS 16", "Social Science", 1, 4)
nais_31 = Course("NAIS 31", "Social Science", 1, 4)
poli_1 = Course("POLI 1 / 1H", "Social Science", 1, 4)
poli_2 = Course("POLI 2", "Social Science", 1, 4)
poli_3 = Course("POLI 3", "Social Science", 1, 4)
poli_5 = Course("POLI 5", "Social Science", 1, 4)
poli_15 = Course("POLI 15", "Social Science", 1, 4)
poli_16 = Course("POLI 16", "Social Science", 1, 4)
poli_17 = Course("POLI 17 / 17H", "Social Science", 1, 4)
psyc_1 = Course("PSYC 1", "Social Science", 1, 4)
psyc_2 = Course("PSYC 2", "Social Science", 1, 4)
psyc_3 = Course("PSYC 3", "Social Science", 1, 4)
psyc_4 = Course("PSYC 4", "Social Science", 1, 4)
psyc_5 = Course("PSYC 5", "Social Science", 1, 4)
psyc_6 = Course("PSYC 6", "Social Science", 1, 4)
psyc_8 = Course("PSYC 8", "Social Science", 1, 4)
psyc_9 = Course("PSYC 9", "Social Science", 1, 4)
psyc_10g = Course("PSYC 10G", "Social Science", 1, 4)
psyc_10h = Course("PSYC 10H", "Social Science", 1, 4)
psyc_12 = Course("PSYC 12", "Social Science", 1, 4)
psyc_14 = Course("PSYC 14", "Social Science", 1, 4)
psyc_24 = Course("PSYC 24", "Social Science", 1, 4)
soc_1 = Course("SOC 1", "Social Science", 1, 4)
soc_5 = Course("SOC 5", "Social Science", 1, 4)
soc_14 = Course("SOC 14", "Social Science", 1, 4)
soc_20 = Course("SOC 20", "Social Science", 1, 4)
soc_28 = Course("SOC 28", "Social Science", 1, 4)
soc_29 = Course("SOC 29", "Social Science", 1, 4)
soc_35 = Course("SOC 35", "Social Science", 1, 4)
wmst_1 = Course("WMST 1", "Social Science", 1, 4)
wmst_3c = Course("WMST 3C#", "Social Science", 1, 4)
wmst_8 = Course("WMST 8#", "Social Science", 1, 4)
wmst_9 = Course("WMST 9 / 9H", "Social Science", 1, 4)
wmst_12 = Course("WMST 12", "Social Science", 1, 4)
wmst_22 = Course("WMST 22#", "Social Science", 1, 4)
wmst_24 = Course("WMST 24", "Social Science", 1, 4)
wmst_25 = Course("WMST 25#", "Social Science", 1, 4)
wmst_26 = Course("WMST 26#", "Social Science", 1, 4)
wmst_27 = Course("WMST 27#", "Social Science", 1, 4)
wmst_28 = Course("WMST 28", "Social Science", 1, 4)
wmst_29 = Course("WMST 29#", "Social Science", 1, 4)
wmst_31 = Course("WMST 31#", "Social Science", 1, 4)

social_science = [
admj_29, afam_10, afam_11, afam_12a, afam_12b, afam_25, anth_2, anth_3, anth_4, anth_5, anth_6, anth_8, anth_12, arts_3tc,
asam_1, asam_10, asam_11, asam_12, asam_13, asam_22, asam_30, asam_42a, asam_42b, cd_10g, cd_10h, cd_12, ceth_8, ceth_10, ceth_11,
ceth_19, ceth_29, chlx_10, chlx_11, chlx_12, chlx_26, comm_7, econ_1, econ_2, econ_3, econ_4,
econ_5, es_1, es_3, es_4, ftv_10, ftv_10h, geo_4, geo_5, geo_10, hist_3a, hist_3b, hist_3c, hist_3ch, hist_6a,
 hist_6b, hist_6c, hist_6ch, hist_7a, hist_7b, hist_9, hist_10, hist_16a, hist_16b, hist_17a,
 hist_17b, hist_17c, hist_18a, hist_18b, hist_19a, hist_19b, huma_10, ics_7, ics_7h, ics_16a,
ics_16b, ics_17, ics_19, ics_25, ics_26, ics_27, ics_36, ics_37, ics_38a, ics_38b, ics_47, intl_5, intl_8, intl_33,
jour_2, knes_47, nais_11, nais_12, nais_16, nais_31, poli_1, poli_2, poli_3, poli_5, poli_15, poli_16, poli_17,
psyc_1, psyc_2, psyc_3, psyc_4, psyc_5, psyc_6, psyc_8, psyc_9, psyc_10g, psyc_10h, psyc_12, psyc_14, psyc_24, soc_1, soc_5,
soc_14, soc_20, soc_28, soc_29, soc_35, wmst_1, wmst_3c, wmst_8, wmst_9, wmst_12, wmst_22, wmst_24, wmst_25, wmst_26,
wmst_27, wmst_28, wmst_29, wmst_31
]

astr_4 = Course("ASTR 4", "Physical Science", 1, 4)
astr_4_15l = Course("ASTR 4/15L", "Physical Science", 1, 4)
astr_10 = Course("ASTR 10", "Physical Science", 1, 4)
astr_10_15l = Course("ASTR 10/15L", "Physical Science", 1, 4)
chem_1a = Course("CHEM 1A / 1AH", "Physical Science", 2, 4)
chem_1b = Course("CHEM 1B / 1BH", "Physical Science", 2, 4)
chem_1c = Course("CHEM 1C / 1CH", "Physical Science", 2, 4)
chem_10 = Course("CHEM 10*", "Physical Science", 2, 4)
chem_25 = Course("CHEM 25*", "Physical Science", 2, 4)
chem_30a = Course("CHEM 30A*", "Physical Science", 2, 4)
chem_30b = Course("CHEM 30B", "Physical Science", 2, 4)
geo_1 = Course("GEO 1", "Physical Science", 1, 4)
geol_10 = Course("GEOL 10", "Physical Science", 1, 4)
geol_20 = Course("GEOL 20", "Physical Science", 1, 4)
met_10 = Course("MET 10", "Physical Science", 1, 4)
met_10_10l = Course("MET 10/10L", "Physical Science", 1, 4)
met_10_20l = Course("MET 10/20L", "Physical Science", 1, 4)
met_12 = Course("MET 12", "Physical Science", 1, 4)
met_12_20l = Course("MET 12/20L", "Physical Science", 1, 4)
phys_2a = Course("PHYS 2A", "Physical Science", 2, 4)
phys_4a = Course("PHYS 4A", "Physical Science", 2, 4)
phys_10 = Course("PHYS 10*", "Physical Science", 2, 4)

physical_science = [
astr_4, astr_4_15l, astr_10, astr_10_15l, chem_1a, chem_1b, chem_1c, chem_10,
chem_25, chem_30a, chem_30b, geo_1, geol_10, geol_20, met_10, met_10_10l, met_10_20l, met_12, met_12_20l,
phys_2a, phys_4a, phys_10
]

anth_1 = Course("ANTH 1 / 1H", "Biological Science", 1, 4)
anth_1_1l = Course("ANTH 1/1L", "Biological Science", 1, 4)
anth_1h_1l = Course("ANTH 1H/1L", "Biological Science", 1, 4)
anth_7 = Course("ANTH 7", "Biological Science", 1, 4)
biol_6a = Course("BIOL 6A / 6AH", "Biological Science", 2, 4)
biol_6b = Course("BIOL 6B / 6BH", "Biological Science", 2, 4)
biol_6c = Course("BIOL 6C / 6CH", "Biological Science", 2, 4)
biol_10 = Course("BIOL 10 / 10H", "Biological Science", 2, 4)
biol_11 = Course("BIOL 11*", "Biological Science", 2, 4)
biol_13 = Course("BIOL 13", "Biological Science", 2, 4)
biol_15 = Course("BIOL 15", "Biological Science", 2, 4)
biol_26 = Course("BIOL 26", "Biological Science", 2, 4)
biol_40c = Course("BIOL 40C", "Biological Science", 2, 4)
esci_1 = Course("ESCI 1", "Biological Science", 1, 4)
esci_1_1l = Course("ESCI 1/1L", "Biological Science", 1, 4)
esci_19 = Course("ESCI 19*", "Biological Science", 1, 4)

biological_science = [
anth_1, anth_1_1l, anth_1h_1l, anth_7, biol_6a, biol_6b, biol_6c, biol_10,
 biol_11, biol_13, biol_15, biol_26, biol_40c, esci_1, esci_1_1l, esci_19
]
#Igetc pref offered
igetc_prefs = {
    "ARTS": "Arts",
    "DANC": "Arts",
    "E S": "Arts",
    "F/TV": "Arts",
    "HUMI": "Arts",
    "INTL": "Arts",
    "MUSI": "Arts",
    "NAIS": "Arts",
    "PHTG": "Arts",
    "THEA": "Arts",
    "WMST": "Arts",
    "EWRT": "English Composition",
    "COMM": "Critical Thinking-English Composition",
    "PHIL": "Critical Thinking-English Composition",
    "MATH": "Mathematics",
    "AFAM": "Humanities",
    "ASAM": "Humanities",
    "CETH": "Humanities",
    "CHLX": "Humanities",
    "ESL": "Humanities",
    "ELIT": "Humanities",
    "EWRT": "Humanities",
    "FTV": "Humanities",
    "FREN": "Humanities",
    "GERM": "Humanities",
    "HNDI": "Humanities",
    "HIST": "Humanities",
    "HUMI": "Humanities",
    "ICS": "Humanities",
    "INTL": "Humanities",
    "ITAL": "Humanities",
    "JAPN": "Humanities",
    "KORE": "Humanities",
    "LING": "Humanities",
    "MAND": "Humanities",
    "NAIS": "Humanities",
    "PERS": "Humanities",
    "PHIL": "Humanities",
    "RUSS": "Humanities",
    "SIGN": "Humanities",
    "SPAN": "Humanities",
    "VIET": "Humanities",
    "WMST": "Humanities",
    "ADMJ": "Social Science",
    "ANTH": "Social Science",
    "ARTS": "Social Science",
    "ASAM": "Social Science",
    "CD": "Social Science",
    "CHLX": "Social Science",
    "COMM": "Social Science",
    "ECON": "Social Science",
    "E S": "Social Science",
    "F/TV": "Social Science",
    "GEO": "Social Science",
    "HIST": "Social Science",
    "HUMA": "Social Science",
    "ICS": "Social Science",
    "INTL": "Social Science",
    "JOUR": "Social Science",
    "KNES": "Social Science",
    "NAIS": "Social Science",
    "POLI": "Social Science",
    "PSYC": "Social Science",
    "SOC": "Social Science",
    "WMST": "Social Science",
    "ASTR": "Physical Science",
    "CHEM": "Physical Science",
    "GEO": "Physical Science",
    "GEOL": "Physical Science",
    "MET": "Physical Science",
    "PHYS": "Physical Science",
    "ANTH": "Biological Science",
    "BIOL": "Biological Science",
    "ESCI": "Biological Science"
}
#All of the sections offered by DeAnza
prefix_options = {
  "ACCT": {"name": "Accounting-DA", "credits": 5, "difficulty": 1},
  "ADMJ": {"name": "Administration of Justice-DA", "credits": 4, "difficulty": 1}, 
  "AFAM": {"name": "African American Studies-DA", "credits": 4, "difficulty": 1},
  "ANTH": {"name": "Anthropology-FD", "credits": 4, "difficulty": 1},
  "ASAM": {"name": "Asian-American Studies-DA", "credits": 5, "difficulty": 1},
  "ASTR": {"name": "Astronomy-FD", "credits": 5, "difficulty": 1},
  "AUTO": {"name": "Automotive Technology-DA", "credits": 4, "difficulty": 1},
  "BIOL": {"name": "Biology-FD", "credits": 5, "difficulty": 2},
  "BUS": {"name": "Business-FD", "credits": 5, "difficulty": 1},
  "CLP": {"name": "Career Life Planning-DA", "credits": 4, "difficulty": 1},
  "CHEM": {"name": "Chemistry-FD", "credits": 5, "difficulty": 1},
  "CHLX": {"name": "Chicanx/Latinx Studies-DA", "credits": 4, "difficulty": 1},
  "C D": {"name": "Child Development-DA", "credits": 4, "difficulty": 1}, 
  "COMM": {"name": "Communication Studies-FD", "credits": 5, "difficulty": 1},
  "CETH": {"name": "Comparative Ethnic Studies-DA", "credits": 4, "difficulty": 1},
  "CIS": {"name": "Computer Information System-FD", "credits": 4.5, "difficulty": 2},
  "COUN": {"name": "Counseling-DA", "credits": 4, "difficulty": 1},
  "DANC": {"name": "Dance-FD", "credits": 4, "difficulty": 1},
  "DMT": {"name": "Design & Manufacturing Tech-DA", "credits": 4, "difficulty": 1},
  "ECON": {"name": "Economics-FD", "credits": 4, "difficulty": 1},
  "EDUC": {"name": "Education-FD", "credits": 4, "difficulty": 1},
  "EDAC": {"name": "Educational Access-DA", "credits": 4, "difficulty": 1},
  "ENGR": {"name": "Engineering-FD", "credits": 4.5, "difficulty": 1},
  "ESL": {"name": "English as a Second Lang-FD", "credits": 0, "difficulty": 1}, 
  "ELIT": {"name": "English/Literature-DA", "credits": 5, "difficulty": 1},
  "EWRT": {"name": "English/Writing-DA", "credits": 5, "difficulty": 1},
  "ESCI": {"name": "Environmental Science-DA", "credits": 4, "difficulty": 1},
  "E S": {"name": "Environmental Studies-DA", "credits": 4, "difficulty": 1},
  "F/TV": {"name": "Film & Television Product-DA", "credits": 4, "difficulty": 1},
  "FREN": {"name": "French-FD", "credits": 5, "difficulty": 1},
  "GEO": {"name": "Geography-DA", "credits": 4, "difficulty": 1},
  "GEOL": {"name": "Geology-FD", "credits": 4, "difficulty": 1},
  "GERM": {"name": "German-FD", "credits": 5, "difficulty": 1},
  "HTEC": {"name": "Health Technologies-DA", "credits": 2, "difficulty": 1},
  "HLTH": {"name": "Health-FD", "credits": 2, "difficulty": 1},
  "HNDI": {"name": "Hindi-DA", "credits": 5, "difficulty": 1},
  "HIST": {"name": "History-FD", "credits": 5, "difficulty": 1},
  "HUMA": {"name": "Human Development-DA", "credits": 4, "difficulty": 1},
  "HUMI": {"name": "Humanities-DA", "credits": 4, "difficulty": 1},
  "ICS": {"name": "Intercultural Studies-DA", "credits": 4, "difficulty": 1},
  "INTL": {"name": "International Studies-DA", "credits": 4, "difficulty": 1},
  "ITAL": {"name": "Italian-FD", "credits": 5, "difficulty": 1},
  "JAPN": {"name": "Japanese-FD", "credits": 5, "difficulty": 1},
  "JOUR": {"name": "Journalism-DA", "credits": 4, "difficulty": 1},
  "KNES": {"name": "Kinesiology-DA", "credits": 1, "difficulty": 1},
  "KORE": {"name": "Korean-FD", "credits": 5, "difficulty": 1},
  "LART": {"name": "Language Arts-DA", "credits": 3, "difficulty": 1},
  "LRNA": {"name": "Learning Assistance-DA", "credits": 1, "difficulty": 1},
  "L S": {"name": "Learning Strategies-DA", "credits": 1, "difficulty": 1},
  "LIB": {"name": "Library-DA", "credits": 1, "difficulty": 1},
  "LING": {"name": "Linguistics-FD", "credits": 4, "difficulty": 1},
  "MAND": {"name": "Mandarin-DA", "credits": 5, "difficulty": 1},
  "MATH": {"name": "Mathematics-FD", "credits": 5, "difficulty": 1}, 
  "MET": {"name": "Meteorology-FD", "credits": 5, "difficulty": 1},
  "MUSI": {"name": "Music-DA", "credits": 4, "difficulty": 1},
  "NAIS": {"name": "Native Americ, Indigenous-DA", "credits": 4, "difficulty": 1},
  "NURS": {"name": "Nursing-DA", "credits": 1, "difficulty": 1},
  "NUTR": {"name": "Nutrition-DA", "credits": 1, "difficulty": 1},
  "PARA": {"name": "Paralegal Program-DA", "credits": 4, "difficulty": 1},
  "PHIL": {"name": "Philosophy-FD", "credits": 4, "difficulty": 1},
  "PHTG": {"name": "Photography-DA", "credits": 3, "difficulty": 1},
  "P E": {"name": "Physical Education-DA", "credits": 1, "difficulty": 1},
  "PEA": {"name": "Physical Education/Adapted-DA", "credits": 1, "difficulty": 1},
  "PHYS": {"name": "Physics-FD", "credits": 6, "difficulty": 2},
  "POLI": {"name": "Political Science-FD", "credits": 5, "difficulty": 2},
  "PSYC": {"name": "Psychology-FD", "credits": 4, "difficulty": 1},
  "REST": {"name": "Real Estate-DA", "credits": 4, "difficulty": 1},
  "RUSS": {"name": "Russian-FD", "credits": 5, "difficulty": 1},
  "SIGN": {"name": "Sign Language-DA", "credits": 5, "difficulty": 1},
  "SOSC": {"name": "Social Science-FD", "credits": 2, "difficulty": 1},
  "SOC": {"name": "Sociology-FD", "credits": 4, "difficulty": 1},
  "SPAN": {"name": "Spanish-FD", "credits": 5, "difficulty": 1},
  "THEA": {"name": "Theater Arts-DA", "credits": 4, "difficulty": 1},
  "VIET": {"name": "Vietnamese Language-DA", "credits": 5, "difficulty": 1},
  "ARTS": {"name": "Visual Arts and Design-DA", "credits": 4, "difficulty": 1}, 
  "WMST": {"name": "Women's Studies-DA", "credits": 4, "difficulty": 1},
}

requirements_data = {
    "English Composition": {"courses" : 1, "discipline":1},
    "Critical Thinking-English Composition":{"courses" : 1, "discipline":1},
    "Mathematics": {"courses" : 1, "discipline" : 1},
    "Arts": {"courses" : 2, "discipline" : 1},
    "Humanities": {"courses" : 1, "discipline" : 1},
    "Social Science": {"courses": 3, "discipline" : 2},
    "Physical Science": {"courses" : 1, "discipline" : 1},
    "Biological Science": {"courses" : 1, "discipline" : 1 },
    "Lab Science" : {"courses" : 1, "discipline" : 1}
}
lab = [chem_1a, chem_1b, chem_1c, chem_10,
chem_25, chem_30a, chem_30b, geo_1, geol_10, geol_20, met_10, met_10_10l, met_10_20l, met_12, met_12_20l,
phys_2a, phys_4a, phys_10,chem_1a, chem_1b, chem_1c, chem_10, chem_25, chem_30a, chem_30b]
lab_set = set(lab)

subject_to_courses = {
    "English Composition" : english_comm,
    "Critical Thinking-English Composition" : english_composition,
    "Mathematics" : mathematics,
    "Arts" : art,
    "Humanities" : humanities,
    "Social Science": social_science,
    "Physical Science" : physical_science,
    "Biological Science" : biological_science,
}


igetc_rankings = {
    "English Composition" : {"EWRT": 1},
    "Critical Thinking-English Composition" : {"COMM": 2, "PHIL": 1},
    "Mathematics" : {
            "MATH":1
            },
    "Arts" : {
            "ARTS":  2, "DANC": 1, "E S": 1, "F/TV":  1, "HUMI":  1, "INTL":  1, "MUSI":  2, "NAIS":  1, "PHTG":  2, "THEA":  1, "WMST":  1
            },
    "Humanities" : {
            "AFAM": 1, "ASAM": 1, "CETH": 1,"CHLX": 1,"ELIT": 1,"EWRT": 1,"FTV": 1,"FREN": 1,"GERM": 1,
            "HNDI": 1,"HIST": 1,"HUMI": 2,"ICS": 1,"INTL": 1,"ITAL": 1, "JAPN": 1,"KORE": 1,"LING": 1,"MAND": 1,"NAIS": 1, "PERS": 1,
            "PHIL": 1,"RUSS": 1,"SIGN": 1,"SPAN": 1,"VIET": 1,"WMST": 1 },
    "Social Science": {  "ADMJ": 1,
            "ANTH": 1,"ARTS": 1,"ASAM": 1,"CD": 1,"CHLX": 1, "COMM": 1,"ECON": 2,"E S": 1,"F/TV": 1,"GEO": 1,"HIST": 2,
            "HUMA": 2, "ICS": 1,"INTL": 1,"JOUR": 1,"KNES": 1,"NAIS": 1,"POLI": 1,"PSYC": 2, "SOC": 1,"WMST": 1},
    "Physical Science" : {"ASTR": 1, "CHEM": 2, "GEO": 1, "GEOL": 1, "MET": 1, "PHYS": 2},
    
    "Biological Science" : {"ANTH": 1, "BIOL":2, "ESCI":1},
}