import os
import utils
import model
import tensorflow as tf
tf.config.run_functions_eagerly(True)

class train():
    '''
    Class used to train the model used in deep fake image detection
    INPUT : train_path, val_path, epochs, batch_size, steps
    train_path = absolute path of the training image set
    val_path = absolute path of the calidation image set
    epochs = Number of epochs to be used for training the model
    batch_size = Batch size to be used per step
    steps = Number of steps to be used per epoch
    '''
    def __init__(self, train_path, val_path):
        self.train_path = train_path
        self.val_path = val_path
        here = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.join(here, "models")
    
    def get_files(self):
        self.train_files, self.label_files = utils.get_files(self.train_path, 'png')
        self.val_files, self.label_files = utils.get_files(self.val_path, 'png')

    @tf.function
    def train(self, model, path, epochs, batch_size, steps, dim):
        '''
        Fucntion used to train the model
        '''
        model.compile('Adam', loss = tf.keras.losses.CategoricalCrossentropy(), metrics = ['accuracy'])
        
        checkpoint_filepath = path
        #model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_filepath, save_best_only=True, 
        #                                                                save_weights_only=False, monitor='val_accuracy', mode='max')

        model.fit(utils.image_generator(self.train_files, self.label_files, batch_size, dim), epochs = epochs, steps_per_epoch = steps,
                        validation_data =utils.image_generator(self.val_files, self.label_files, batch_size, dim),
                        validation_steps=15)

    
    def run(self, epochs, batch_size, steps, dim=(299, 299)):
        '''
        DRIVER FUNCTION
        '''
        self.get_files()
        print("************TRAINING SOFT ATTENTION BASED DEEP FAKE DETECTION MODEL************")
        mod = model.model(1024, 19)
        self.train(mod, self.path, epochs, batch_size, steps, dim)
