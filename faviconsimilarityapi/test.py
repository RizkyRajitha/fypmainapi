from imagepro import imageutil
import time
# data = findimage()

dictdata = imageutil.image_data_dict

queryimg = imageutil.get_image_data_from_path_cv('./unknownFaviconsq/zoom_us.ico')
# queryimg = imageutil.get_image_data_from_path_cv('./unknownFaviconsq/zoom_us.ico')
# queryimg = imageutil.get_image_data_from_path_cv('./unknownFaviconsq/zoom_us.ico')
# queryimg = imageutil.get_image_data_from_path_cv('./unknownFaviconsq/zoom_us.ico')
# queryimg = imageutil.get_image_data_from_path_cv('./unknownFaviconsq/zoom_us.ico')
# queryimg = imageutil.get_image_data_from_path_cv('./unknownFaviconsq/zoom_us.ico')


start = time.time()
print(start)

# for q1 in [queryimg,queryimg,queryimg,queryimg,queryimg,queryimg,queryimg,queryimg,queryimg,queryimg]:
#     for idex , img in enumerate(dictdata.keys()):
#         # print(img)
#         # print(dictdata[img])
        
#         # candidateImg = image_data_dict[icon+".ico"]
#         # queryImg = get_image_data_from_path_cv(query_img_path)
#         # candidateImg = imageutil.get_image_data_from_path_cv("./favicons/"+img)


#         res = imageutil.compareFavs( "MSE", 10 , dictdata[img] ,q1)
#         # print(res)
#         if res:
#             print(idex)
#             print(img)
#             break
#             # return img

print(time.time())
print(time.time()-start)


start = time.time()
print(start)

# for q1 in [queryimg,queryimg,queryimg,queryimg,queryimg,queryimg,queryimg,queryimg,queryimg,queryimg]:
#     for idex , img in enumerate(dictdata.keys()):
#         # print(img)
#         # print(dictdata[img])
        
#         # candidateImg = image_data_dict[icon+".ico"]
#         # queryImg = get_image_data_from_path_cv(query_img_path)
#         # candidateImg = imageutil.get_image_data_from_path_cv("./favicons/"+img)


#         res = imageutil.compareFavs( "MSE", 10 , dictdata[img] ,q1)
#         # print(res)
#         if res:
#             print(idex)
#             print(img)
#             break
#             # return img

print(time.time())
print(time.time()-start)