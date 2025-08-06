import matplotlib.pyplot as plt
import seaborn as sns

def correlation_matrix_heatmap(df, output_file=None, identifier=None):
    corr_matrix = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 8), dpi=300)

    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm",
            square=True, linewidths=0.5, cbar_kws={"shrink": 0.5}, vmin=-1, vmax=1)

    plot_title = "Correlation matrix heatmap"
    if identifier:
        plot_title += f" - {identifier}"
    plt.title(plot_title)
    
    plt.tight_layout()
    
    if output_file:
        plt.savefig(output_file + ".png")
    
    plt.show()

def split_data(df, response):
    X = df.drop(response, axis=1)
    y = df[response]
    
    return(X, y)