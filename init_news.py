# coding: utf-8
from datetime import datetime
from redis_news import RedisNews

list_news = [
	{
		"title" : "朝鲜特种部队视频公布 展示士兵身体素质与意志",
		"img_url" : "/static/img/news/01.png",
		"content" : "20世纪90年代初，朝鲜人民军在部分改革后变成一支既能进行传统战争、实施特种作战，又能两者高效结合进行合成作战的部队。目前，特点是立足于游击战、灵活机动、战斗力超强。朝鲜特种部队具体人数目前不详，估计在8.8-12.15万人之间。朝鲜特种部队是在金日成南进作战思想下组建的",
		"is_valid" : True,
		"news_type" : "推荐",
		'created_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		'updated_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	},
	{
		"title" : "男子长得像'祁同伟'挨打 打人者:为何加害检察官",
		"img_url" : "/static/img/news/04.jpg",
		"content" : "因与热门电视剧中人物长相相近，男子竟然招来一顿拳打脚踢。4月19日，打人男子周某被抓获。\r\n\r\n半个月前，酒后的周某看到KTV里有一名男子很像电视剧中的反派。二话不说，周某冲上去就问你为什么要加害检察官？男子莫名其妙，回了一句神经病。\r\n\r\n周某一听气不打一处来，对着男子就是一顿拳打脚踢，嘴里面还念叨着，“叫你加害检察官，我打死你！”随后，周某趁机逃走。受伤男子立即报警，周某被上海警方上网通缉。\r\n\r\n据民警调查，22岁的男子周某是湖南辰溪人。从4月初开始，周某迷上了一部热播剧。因剧里面的检察官受到公安厅长的加害，周某心中对公安厅长这个角色愤恨不已。有时，周某甚至对身边的朋友说：“如果再让我见到他，肯定好好教训他一顿！”\r\n\r\n周某犯案后，见情况不妙当天逃回湖南怀化老家躲避。半个月后，他准备再次外出打工。4月19日，周某在怀化火车站乘车时被民警发现，当场将其抓获，周某对自己的违法事实供认不讳。\r\n\r\n无独有偶，《人民的名义》火了，也让一些“追星”入迷，如果说上面这个故事的人比较冤枉外，而下面这位则是“入戏”太深，干出这样的荒唐之事。",
		"is_valid" : True,
		"news_type" : "百家",
		'created_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		'updated_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	},
	{
		"title" : "导弹来袭怎么办？日本政府呼吁国民躲入地下通道",
		"img_url" : "/static/img/news/03.jpg",
		"content" : "“先锋”导弹的实质是高超声速飞行器。通常，高超声速飞行器是指飞行速度超过5倍声速的飞行器。近年来，除了洲际弹道导弹等传统高超声速飞行器外，临近空间吸气式高超声速巡航飞行器、临近空间助推滑翔飞行器、小型跨大气层空间机动飞行器这三类高超声速飞行器也逐渐登上历史舞台。\r\n\r\n据悉，“先锋”导弹是吸气式巡航飞行器与助推滑翔飞行器的结合，采用大型火箭助推器作为运送载体，具有大速度机动、强耐温耐蚀、高概率突防等显著特征。\r\n\r\n大速度机动。“先锋”导弹的飞行器，采用了高升阻比的升力体结构。升力体结构布局有助于提高飞行器的升阻比，相同初始速度下，升阻比越高，飞行器纵向滑跃距离越远，横向机动和空防能力越强。这有利于“先锋”导弹飞行器获得较大的内部空间，同时具备良好的气动性能。作战行动时，“先锋”导弹由助推加速器带到100千米的太空和地球大气层边缘，达到该高度后，飞行器冲出大气层并做自由段飞行，达到预期的高超声速，最大飞行速度可达20马赫。按这一速度计算，“先锋”导弹在15分钟内便可由俄罗斯境内飞抵美国华盛顿。这一飞行速度不仅远大于各国现役巡航导弹，而且留给对手的反应时间也远小于洲际弹道导弹。\r\n\r\n强耐温耐蚀。由于“先锋”导弹穿越大气层进行高超声速飞行，弹头表面温度会因气动加热升至1600℃至2000℃。为解决这一问题，“先锋”导弹采用了多种高强度、耐高温、抗腐蚀、低密度结构的新型材料，如超高温陶瓷材料、金属基复合材料等。同时，“先锋”导弹机体内部设置有多层隔热措施保护内部结构和机载设备。这使得“先锋”导弹能在极端条件下保持稳固，同时还能抵御激光武器照射，确保了弹头在等离子环境下长期安全飞行。\r\n\r\n高概率突防。“先锋”导弹由大型火箭助推器运载，既能保障发射助推段的机动灵活、快速响应，又可以为飞行器提供足够的初始速度，而且未来可能在陆基、空基和天基多平台发射。因此，“先锋”导弹同传统巡航导弹相比，能够进行更为复杂的航迹规划和战术机动。它能够从任意方向和不同高度范围接近目标，有效规避他国反导系统半球形探测区域，达到快速隐蔽突防的效果。在接近目标时，“先锋”导弹能够实现数千公里侧向深度机动和大幅高度机动，以绕过导弹防御系统并躲避拦截弹，对目标实施有效打击。按照俄罗斯宣称，现役的一切导弹拦截系统，将在“先锋”面前形同虚设。",
		"is_valid" : True,
		"news_type" : "本地",
		'created_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		'updated_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	},
	{
		"title" : "美媒:朝在建能发射3发以上导弹的3000吨级新潜艇",
		"img_url" : "/static/img/news/04.jpg",
		"content" : "据韩联社4月21日报道，美国保守媒体《华盛顿自由灯塔》20日引用联合国报告报道称，朝鲜可能对“新浦”级潜艇进行改装，使其可连发多枚潜射导弹，韩国军方负责人21日对此表示，需进一步分析，持谨慎态度。\r\n\r\n韩国军方人士当天表示，朝鲜投入“新浦”级潜艇试射潜射导弹，但是否完成了发射管改造仍需缜密分析。该人士还补充道，这一说法不属实的可能性较大。\r\n\r\n美媒称，朝鲜“新浦”级潜艇只有一根发射管，一次只能发射一枚潜射导弹， 但朝鲜正在建造能发射3发以上的3000吨级新型潜艇。",
		"is_valid" : True,
		"news_type" : "推荐",
		'created_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		'updated_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	},
	{
		"title" : "证监会:前发审委员冯小树违法买卖股票被罚4.99亿",
		"img_url" : "/static/img/news/08.jpg",
		"content" : "张晓军说，证监会对冯小树违法买卖股票行为的查处，不折不扣落实了中央巡视整改意见，充分体现了证监会打铁还需自身硬的责任意识与勇于直面问题的使命担当。证监会将秉持依法、全面、从严的监管原则，对证券期货违法违规行为保持高压态势，牢牢守住不发生系统性金融风险底线。对系统干部自身违法行为绝不姑息，依法严厉惩处，持续加大问责力度，正人先正己，推动全面从严治党向纵深发展，坚定维护金融秩序，促进金融业安全运行。",
		"is_valid" : True,
		"news_type" : "百家",
		'created_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		'updated_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	},
	{
		"title" : "外交部回应安倍参拜靖国神社:同军国主义划清界限",
		"img_url" : "/static/img/news/new1.jpg",
		"content" : "据报道，日本首相安倍晋三当天向靖国神社春季例行大祭供奉了“真榊”祭品，日本首相助理、总务大臣以及90多名国会议员集体前往参拜。在回答相关提问时，陆慷作上述表示。他说：“靖国神社供奉着对侵略战争负有直接责任的二战甲级战犯，我们一贯坚决反对日本政要的错误做法。中方敦促日方恪守中日四个政治文件精神，切实落实中日四点原则共识，正视和深刻反省侵略历史，同军国主义划清界限，以实际行动取信于亚洲邻国和国际社会。”",
		"is_valid" : True,
		"news_type" : "推荐",
		'created_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		'updated_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	},
	{
		"title" : "“萨德”供地违法？韩民众联名起诉要求撤回供地",
		"img_url" : "/static/img/news/new1.jpg",
		"content" : "据韩联社4月21日报道，韩国律师团体“民主社会律师聚会”当天表示，396名星州当地民众联名向首尔行政法院起诉，要求撤回向“萨德”供地的批复，诉讼对象为韩国外交部长。民众申请在本案宣判前，暂停向“萨德”供地的协议效力。",
		"is_valid" : True,
		"news_type" : "推荐",
		'created_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		'updated_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
	},
	{
		"title" : "美国四处点火，到底图什么？专家这一席话，懂了",
		"img_url" : "/static/img/news/01.png",
		"content" : "从本月22日起，欧盟委员会将针对美国钢铝关税采取反制措施，对总额达28亿欧元，约合210亿元人民币的美国商品征收25%的额外关税。涉及的产品包括蔓越莓、橙汁、花生酱、牛仔裤、化妆品、摩托车和钢铁制品等。\r\n\r\n　　欧盟此举是为了反制美国从6月1号开始对欧盟、加拿大和墨西哥的钢铝产品分别征收25%和10%的关税而采取的行动。不仅是欧盟，包括日本、加拿大、墨西哥、印度、俄罗斯等国，也都纷纷出台反制措施，一场贸易大战，在全球蔓延。\r\n\r\n　　贸易乱战怎么破？ 6月21日《央视财经评论》请来了商务部研究院区域研究中心主任张建平和央视财经评论员马光远做客演播室，对此进行了深度解读。",
		"is_valid" : True,
		"news_type" : "推荐",
		'created_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
		'updated_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	}
]

def main():
	""" 初始化新闻数据 """
	news = RedisNews()
	news.init_news(list_news)
	print(news.get_all_news())

if __name__ == '__main__':
	main()