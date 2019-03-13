aantal_testgevallen = int(input())
for geval in range(aantal_testgevallen):
    info_v_n = input().split()
    vetraging = int(info_v_n[0])
    aantal_vluchten = int(info_v_n[1])

    uren_minuten_ver_aan = input().split()

    minutentotaal_aankomst_laatst = (int(uren_minuten_ver_aan[3]) + (int(uren_minuten_ver_aan[2]) * 60) + vetraging) % 1440

    for i in range(1, aantal_vluchten):
        uren_minuten_ver_aan = input().split()

        minutentotaal_vetrek_i = int(uren_minuten_ver_aan[1]) + (int(uren_minuten_ver_aan[0]) * 60)
        minutentotaal_aankomst_i = int(uren_minuten_ver_aan[3]) + (int(uren_minuten_ver_aan[2]) * 60)

        if (minutentotaal_vetrek_i - minutentotaal_aankomst_laatst) % 1440 < 60:
            minutentotaal_aankomst_i += 60 - ((minutentotaal_vetrek_i - minutentotaal_aankomst_laatst) % 1440)

        minutentotaal_aankomst_laatst = minutentotaal_aankomst_i

    print(geval + 1, minutentotaal_aankomst_laatst // 60, minutentotaal_aankomst_laatst % 60)