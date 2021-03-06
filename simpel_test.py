from models.model_factory import get_model

if __name__ == "__main__":

    # model_names = ['ResNest50','ResNest101','ResNest200','ResNest269']
    model_names = ['ResNest50']
    # model_names = ['RegNetX400','RegNetX1.6','RegNetY400','RegNetY1.6']
    input_shape = [224,224,3]
    n_classes=81
    fc_activation='softmax' #softmax sigmoid

    for model_name in model_names:
        print('model_name',model_name)
        model = get_model(model_name=model_name,input_shape=input_shape,n_classes=n_classes,
                    verbose=True,fc_activation=fc_activation,using_cb=True)
        print('-'*10)

    #RegNetY600 set
    # model = get_model(model_name="RegNet",input_shape=input_shape,n_classes=n_classes,
    #             verbose=True,fc_activation=fc_activation,stage_depth=[1,3,7,4],
    #             stage_width=[48,112,256,608],stage_G=16,SEstyle_atten="SE",active='mish')
    # print('-'*10)