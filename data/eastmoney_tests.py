import eastmoney as et
import csindex as ci
import cn

csi = ci.cnSecurityIndustry()
for v in csi:
    charts = et.cn_chartbar(cn.codeToSymbol(v['securityCode']))
    print(len(charts))
